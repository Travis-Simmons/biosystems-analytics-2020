# TIFF metadata tool 
High-throughput phenotyping has become quite popular in recent years. Various sensors are used to collect images at a whole field level. It is quite often that images may not have the correct GPS coordinates. This script allows you to load a set of images that need to be corrected and a CSV file that contains image filenames and bounding coordinates (Upper left, lower left, upper right, lower right, and center). The script will open each image using GDAL, replace current coordinates, and output a new image file with updated coordinates. 

## Running the program 
* First, install dependencies by running the following command: `./depend.sh`

* You're now ready to go! Just run the following: `./edit_gps.py <image directory> -c <CSV file path>`

* The default output directory is `gpscorrect_out/` but you can specify a directory by using the following flag: `-o <output directory>`
