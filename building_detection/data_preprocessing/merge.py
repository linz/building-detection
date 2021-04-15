"""
Simple script for merging prediction outputs and
dissolving adjoining prediction objects
"""

import os

import click
import fiona
from shapely.geometry import mapping, shape
from shapely.ops import cascaded_union


def merge_datasets(directory, merged_file):
    """
    Merge all geojson files in prediction dir
    """

    file_list = os.listdir(directory)
    json_files = [filename for filename in file_list if filename.endswith(".json")]

    meta = fiona.open(os.path.join(directory, json_files[0])).meta
    with fiona.open(merged_file, "w", **meta) as output:
        for file in json_files:
            for features in fiona.open(os.path.join(directory, file)):
                output.write(features)


def dissolve_features(merged_file, dissolved_file):
    """
    Dissolve adjoining prediction features
    """

    with fiona.open(merged_file, "r") as ds_in:
        crs = ds_in.crs
        drv = ds_in.driver

        filtered = filter(lambda x: shape(x["geometry"]).is_valid, list(ds_in))

        geoms = [shape(x["geometry"]) for x in filtered]
        dissolved = cascaded_union(geoms)

    schema = {"geometry": "Polygon", "properties": {"id": "int"}}

    with fiona.open(dissolved_file, "w", driver=drv, schema=schema, crs=crs) as ds_dst:
        for i, g in enumerate(dissolved):
            ds_dst.write({"geometry": mapping(g), "properties": {"id": i}})


def make_outout_dir(directory):
    """
    As we read all .json files in a dir and merge them, it
    is best not to dump other json files in there as these
    will be merged in on any following execussions
    """

    output_dir = os.path.join(directory, "merged_predictions")
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    return output_dir


@click.command()
@click.option("--directory", "-d", help="The directory where the json files to merged reside")
def merge_predictions(directory):
    """
    1) Merge predictions )json) files &
    2) dissolve adjoining predictions objects
    """

    # Keep the output separate
    output_dir = make_outout_dir(directory)

    # Output file names
    merged_filename = "predictions_merged.json"
    dissolved_filename = "predictions_merged_and_dissolved.json"

    # Path to outputs
    merged_file = os.path.join(output_dir, merged_filename)
    dissolved_file = os.path.join(output_dir, dissolved_filename)

    # Merge files
    merge_datasets(directory, merged_file)

    # Dissolve features formerly accross image boundaires
    dissolve_features(merged_file, dissolved_file)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    merge_predictions()
