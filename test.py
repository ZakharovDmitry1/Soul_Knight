import json

with open('NewCollection.json', 'r') as readfile:
    text = json.load(readfile)['tiles']
    newdict = {}
    for tile in text:
        newdict[int(tile['id'])] = tile['image']

with open('tiles_for_start_map.json', 'w') as writefile:
    json.dump(newdict, writefile)

