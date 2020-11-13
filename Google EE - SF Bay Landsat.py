import ee
from ee_plugin import Map

#Define image source
image = ee.FeatureCollection('LANDSAT/LC08/C01/T1_SR');

#Define image dates & location
image = image.filterDate('2018-02-01','2018-02-20');
image = image.filterBounds(ee.Geometry.Point(-122.1899, 37.5010));

#Pull image with least cloud cover first
least_cloudy = ee.Image(image.sort('CLOUD_COVER').first())

#Define the visualization parameters.
vizParams = {
  'bands': ['B5', 'B4', 'B3'],
  'min': 0,
  'max': 3000,
  'gamma': 1.4
};

#Center the map and display the image.
Map.setCenter(-122.1899, 37.5010, 10); #San Francisco Bay
Map.addLayer(least_cloudy, vizParams, 'SF2018 Infared');

#Print total number of Maps pulled
print('Total number:', image.size().getInfo())
