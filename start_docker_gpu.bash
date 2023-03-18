#!/bin/bash

CONTAINER_NAME=tf_gpu_c
IMAGE_NAME=tf_gpu
CURRENT_DIR=$(pwd)
DATA_ROOT_FOLDER="/media/edge7/TOSHIBA EXT/"
TO_MOUNT_DIR=${TO_MOUNT:-$DATA_ROOT_FOLDER}

docker run --rm -it --name $CONTAINER_NAME \
    --gpus all \
    -p 8889:8889 \
    -v "$CURRENT_DIR:/workspace:rw" \
    -v "$TO_MOUNT_DIR:$TO_MOUNT_DIR:ro" \
    --workdir /workspace \
    $IMAGE_NAME \
    jupyter notebook --port 8889 --ip 0.0.0.0 --allow-root --NotebookApp.token=''

echo "Exited $CONTAINER_NAME container."
