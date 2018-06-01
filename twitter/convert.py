#from sys import argv
#from os.path import exists
import json

f = open('data.json', 'r')
output = open('out.geojson', 'a')

count = 1
for line in f:
    data = json.loads(line)
    geojson = {
           "type": "Feature",
           "properties": { "id": count },
           "geometry" : {
               "type": "Point",
               "coordinates": [data["coordinates"][0], data["coordinates"][1]],
               }
           }
    json.dump(geojson, output)
    output.write(',\n')
    count += 1

f.close()
output.close()