# TIFF metadata tool (TMT) 
High-throughput phenotyping, the use of various sensors to collect plant phenotypic data, has become quite popular in recent years. Often, the images collected may not have the correct GPS coordinates due to slight sensor movement. TMT allows you to load a set of TIFF images that need to be corrected and a CSV file that contains image filenames and bounding coordinates (upper left, lower left, upper right, lower right, and center). The script will open each image using GDAL, replace current coordinates, and output a new image file with updated coordinates. 

## Running the program 

1. install dependencies by running the following command: 
```
./depend.sh
```

2. You're now ready to go! To run the script, just run:
```
./edit_gps.py <image directory> -c <CSV file path>
```

> The default output directory is `gpscorrect_out/` but you can specify a directory by using the following flag: `-o <output directory>`
