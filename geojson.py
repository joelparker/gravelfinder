#!/usr/bin/env python3
import requests
import json

VT_CENTERLINE_GEOJSON_URL='https://opendata.arcgis.com/datasets/1dee5cb935894f9abe1b8e7ccec1253e_39.geojson'

def get_centerline_geojson():
    r = requests.get(VT_CENTERLINE_GEOJSON_URL)
    if r.status_code == 200:
        return r.json()
    return None

def generate_geojson_for_class_range(vt_centerline_geojson,min_road_class=4,max_road_class=7,output_format='./static/class{0}{1}.geojson'):
    if vt_centerline_geojson is not None:
        output_file=output_format.format(min_road_class,max_road_class)
        road_objects = []
        for feature in vt_centerline_geojson['features']:
            if 'properties' in feature and 'AOTCLASS' in feature['properties']:
                road_class = int(feature['properties']['AOTCLASS'])
                if road_class >= min_road_class and road_class <= max_road_class:
                    road_objects.append(feature)
        print(len(road_objects))
        new_json_data = {}
        new_json_data['type']='FeatureCollection'
        new_json_data['features']=road_objects
        with open(output_file,'w') as outfile:
            json.dump(new_json_data,outfile)
                
def generate_geojson_for_class(road_class_to_filter,vt_centerline_geojson,output_format='./static/class{0}.geojson'):
    if vt_centerline_geojson is not None:
        road_objects = []
        for feature in vt_centerline_geojson['features']:
            if 'properties' in feature and 'AOTCLASS' in feature['properties']:
                road_class = int(feature['properties']['AOTCLASS'])
                if road_class == road_class_to_filter:
                    road_objects.append(feature)
        print(len(road_objects))
        new_json_data = {}
        new_json_data['type']='FeatureCollection'
        new_json_data['features']=road_objects
        with open(output_format.format(road_class_to_filter),'w') as outfile:
            json.dump(new_json_data,outfile)

def generate_unpaved_geojson(vt_centerline_geojson,output_file='./static/unpaved.geojson'):
    if vt_centerline_geojson is not None:
        road_objects = []
        for feature in vt_centerline_geojson['features']:
            if 'properties' in feature and 'SURFACETYPE' in feature['properties']:
                surface_type = int(feature['properties']['SURFACETYPE'])
                if surface_type !=1 and surface_type !=9:
                    #skip class 4 and 7 roads
                    if 'AOTCLASS' in feature['properties']:
                        if feature['properties']['AOTCLASS'] not in [4,7]:
                            road_objects.append(feature)
        print(len(road_objects))
        new_json_data = {}
        new_json_data['type']='FeatureCollection'
        new_json_data['features']=road_objects
        with open(output_file,'w') as outfile:
            json.dump(new_json_data,outfile)

def main():
    vt_centerline_geojson=get_centerline_geojson()
    generate_unpaved_geojson(vt_centerline_geojson=vt_centerline_geojson)
    for i in range(4,8):
        print('creating file for class {0}'.format(i))
        generate_geojson_for_class(i,vt_centerline_geojson=vt_centerline_geojson)
    generate_geojson_for_class_range(vt_centerline_geojson=vt_centerline_geojson)

if __name__ == '__main__':
    main()
