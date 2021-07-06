FROM quay.io/azavea/raster-vision:pytorch-0.13.1

# Uncomment once requirements.txt is merged to master
# COPY ./rastervision_building_detection/requirements.txt /opt/src/requirements.txt
# RUN pip install $(grep -ivE "rastervision_*" requirements.txt)

COPY ./building_detection/ /opt/src/building_detection/

ENV PYTHONPATH=/opt/src/building_detection/:$PYTHONPATH

CMD ["bash"]
