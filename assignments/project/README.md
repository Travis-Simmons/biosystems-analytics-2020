# TIFF metadata tool 
High-throughput phenotyping has become quite popular in recent years. Various sensors are used to collect images at a whole field level. It is quite often that images may not have the correct GPS coordinates. This script allows you to load a set of images that need to be corrected and a CSV file that contains image filenames and bounding coordinates (Upper left, lower left, upper right, lower right, and center). The script will open each image using GDAL, replace current coordinates, and output a new image file with updated coordinates. 

## Running the program 
* First, install dependencies
`./depend.sh`

