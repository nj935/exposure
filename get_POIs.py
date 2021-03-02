import pandas as pd
import geopandas as gpd
import os
import pyrosm as pyrosm
import time
import argparse

data = os.getenv('data')

parser = argparse.ArgumentParser()
parser.add_argument("country")
parser.add_argument('poi_type')
#parser.add_argument('-p','--promote',nargs='+',type=int,help='promote item to top')
args = parser.parse_args()
country = args.country
poi_type = args.poi_type

t0 = time.time()

in_pth = data + '/osm/{}/{}-latest.osm.pbf'.format(country,country)
osm = pyrosm.OSM(in_pth)

print('created PYROSM object')

filter = {'amenity': poi_type}
gdf = osm.get_pois(custom_filter=filter)[['name','geometry','amenity']]

#if convert_polygons_to_points:
#    gdf.geometry = [geom.centroid if geom.type in ['Polygon','MultiPolygon'] else geom for geom in gdf.geometry]
    
#if save_shp:
#    out_pth = get_pth(country + '/{}_{}.shp'.format(country,'_'.join(pois)))
#    gdf.to_file(out_pth)
       
t1=time.time()
print("retrieved {} POIs in {:,.0f} seconds".format(len(gdf), t1-t0))
#return(gdf)