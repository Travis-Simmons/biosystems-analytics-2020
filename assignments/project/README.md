# TIFF metadata tool (TMT)
High-throughput phenotyping, the use of various sensors to collect plant phenotypic data, has become quite popular in recent years. It allows scientists to collect phenotypic information in a faster, cheaper manner. However, the images collected may not have the correct GPS coordinates due to slight sensor movement. This creates a significant amount of error when trying to stitch these images together. TMT allows you to correct corner coordinates of TIFF images so that they align correctly. A CSV file that contains image filenames and bounding coordinates must be provided (see CSV format below). The script will open and read each image using GDAL, replace current coordinates with those listed in the CSV file, and output a new image file with updated coordinates.

## CSV format

The CSV file must be in the following format:

|Filename  |Upper left |Lower left |Upper right |Lower right |Center
--- | --- | --- | --- | --- | --- |
image_left.tif|-111.9750534,33.0745881|-111.9750534,33.0745781|-111.9750445,33.0745881|-111.9750445,33.0745781|-111.9750489,33.0745831

## Usage

1. A directory containing TIF images (required)

2. `-c/--csv` CSV file containing updated GPS coordinates (required)

3. `-o/--outdir` Directory where images will be saved (optional)


## Running the program

1. Install dependencies:
```
./depend.sh
```

2. You're ready to go! Run the command to correct the images:
```
./edit_gps.py <image directory> -c <CSV file path>
```

> Note: The default output directory is `gpscorrect_out/`.

## Output images

The corner coordinates of the ouput images will be changed to those listed on the CSV file. You can then visualize your images on QGIS or ArcGIS, and you will see that the geographic placement of the images has changed.
<p align="center">
  <img src="example.png" width="350" title="Output image">
</p>
