rm -rf annotations
mkdir annotations
cd annotations

# download the COCO dataset image information file
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip

# extract the image information file
unzip annotations_trainval2017.zip
rm annotations_trainval2017.zip
mv annotations/instances_val2017.json .

# delete the rest of the files and directories
rm -r annotations

cd ..
# Download IMDB-face CSV
wget https://storage.googleapis.com/public_stuff/IMDb-Face.csv

DATA_ROOT_FOLDER=$1
echo "Creating layout folder in $DATA_ROOT_FOLDER"
rm -rf "$DATA_ROOT_FOLDER/data/"
rm -rf "$DATA_ROOT_FOLDER/data/"

mkdir "$DATA_ROOT_FOLDER/data"
mkdir "$DATA_ROOT_FOLDER/data/person"
mkdir "$DATA_ROOT_FOLDER/data/notperson"

echo "done"