################################################################################
#
#  Create_labels.py
#  Crown copyright (c) 2021. Land Information New Zealand on behalf of
#  the New Zealand Government.
#
#  This file is released under the MIT licence. See the LICENCE file found
#  in the top-level directory of this distribution for more information.
#
################################################################################

"""
Utility for creating labels from LDS data
"""


import json
import os
import urllib.request

import boto3
import click


def get_tile_coordinates(lds_api_key: str, lds_tile_layer: str, lds_tile_id_field: str, tile_id: str) -> list:
    """ Fetch the index tile's coordinates """

    url_lds_topo_tile = (
        "https://data.linz.govt.nz/services;"
        f"key={lds_api_key}"
        f"/wfs?service=WFS"
        "&version=2.0.0"
        "&request=GetFeature"
        f"&typeNames=layer-{lds_tile_layer}"
        f"&cql_filter={lds_tile_id_field}='{tile_id}'"
        "&outputformat=json"
    )

    with urllib.request.urlopen(url_lds_topo_tile) as url:
        data = json.loads(url.read().decode())
        tile_coordinates = data["features"][0]["geometry"]["coordinates"]

    return tile_coordinates


def format_coordinates_for_cql(tile_coordinates: str) -> str:
    """ Format the tile coordinates for the cql filter string """

    cql_filter_string = (
        f"POLYGON(({tile_coordinates[0][1]}+{tile_coordinates[0][0]},"
        f"{tile_coordinates[1][1]}+{tile_coordinates[1][0]},"
        f"{tile_coordinates[2][1]}+{tile_coordinates[2][0]},"
        f"{tile_coordinates[3][1]}+{tile_coordinates[3][0]},"
        f"{tile_coordinates[4][1]}+{tile_coordinates[4][0]}))"
    )

    return cql_filter_string


def get_dataset_filtered_by_tile(
    lds_api_key: str, lds_layer_to_tile: str, cql_filter_string: str, building_source_imagery: str
) -> dict:
    """
    Use the tiles coordinates (as provided by the cql_filter_string) to request a LDS
    layer's features that fall within the index tile's extent.
    """
    source_name = urllib.parse.quote(building_source_imagery.encode("utf8"))

    url = (
        "https://data.linz.govt.nz/services;"
        f"key={lds_api_key}"
        "/wfs?SERVICE=WFS"
        "&VERSION=2.0.0"
        "&srsName=epsg:4326"
        "&REQUEST=GetFeature"
        f"&typeNames=layer-{lds_layer_to_tile}"
        f"&cql_filter=capture_source_name='{source_name}'+AND+intersects(shape,{cql_filter_string})"
        "&outputformat=json"
    )
    with urllib.request.urlopen(url) as url:
        data_by_tile = json.loads(url.read().decode())
    return data_by_tile


def write_data_locally(output_path: str, tile_id: str, data: dict):
    """
    Write the LDS layer's features associated with the index tiles
    to a local directory.
    """

    file_path = os.path.join(output_path, f"{tile_id}.geojson")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_data_to_bucket(output_path: str, aws_profile: str, tile_id: str, data: dict):
    """
    Write the LDS layer's features associated with the index tiles
    to a s3 bucket.
    """

    file_name = f"{tile_id}.geojson"

    session = boto3.session.Session(profile_name=aws_profile)
    s3 = session.resource("s3")
    s3.Bucket(output_path).put_object(Key=file_name, Body=(bytes(json.dumps(data).encode("UTF-8"))))


# - Below formatting is ugly but is controlled by black and is non-negotiable.
# - Click conflicts with pylint as pylint does not see the args passed in by click
# For this reason pylint E1120 has been disbaled for this block.
# - Pylint limits args to 5 however we want the user to have more options than this
# via Click and pylint R0913 has been disabled for this block.


# pylint: disable=E1120
# pylint: disable=R0913
@click.command()
@click.option("--lds-tile-layer", default="104691", help="The LDS layer id for the imagery index tile dataset")
@click.option(
    "--lds-tile-id-field", default="index_tile_id", help="The index tile dataset's attribute name for the tile id field"
)
@click.option("--lds-layer-to-tile", default="101292", help="The id of the lds layer that is to be chunked by index tile")
@click.option(
    "--building-source-imagery",
    default="",
    help="The source imagery of the building outlines. This is to avoid buildings from newer imagery ",
)
@click.option(
    "--tile-id",
    required=True,
    multiple=True,
    help="tile ids from the --lds-tile-layer-id dataset to chunk the --lds-layer-to-tile dataset by",
)
@click.option(
    "--lds-api-key",
    default=lambda: os.environ.get("LDS_API_KEY", ""),
    help="LDS API KEY. Defaults to environment variable LDS_API_KEY",
)
@click.option("--output-path", required=True, help="Where to write the labels output. Either a local path or s3 bucket name")
@click.option(
    "--store-type", default="local", type=click.Choice(["s3", "local"], case_sensitive=False), help="Either 's3' or 'local'"
)
@click.option(
    "--aws-profile",
    default="",
    help="If using --store-type s3, then a AWS profile must be configured and the profile name supplied",
)
def tiles_lds_feature(
    lds_tile_layer: str,
    lds_tile_id_field: str,
    lds_layer_to_tile: str,
    tile_id: str,
    lds_api_key: str,
    output_path: str,
    store_type: str,
    aws_profile: str,
    building_source_imagery: str,
) -> str:
    """ Chunk LDS dataset by LDS index tiles """

    for index_tile in tile_id:
        # Get the coords for the topo index tile
        # These coords will be used to chunk the LDS dataset by tile extent
        tile_coordinates = get_tile_coordinates(lds_api_key, lds_tile_layer, lds_tile_id_field, index_tile)

        # Take the tile extent and translate it to the format required for the cql spatial extent filter
        cql_filter_string = format_coordinates_for_cql(tile_coordinates[0])

        # get dataset filtered by tile
        data = get_dataset_filtered_by_tile(lds_api_key, lds_layer_to_tile, cql_filter_string, building_source_imagery)

        # Write data
        if store_type == "local":
            write_data_locally(output_path, index_tile, data)
        if store_type == "s3":
            write_data_to_bucket(output_path, aws_profile, index_tile, data)


if __name__ == "__main__":
    tiles_lds_feature()
