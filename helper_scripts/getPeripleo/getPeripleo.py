# author: Philipp Gerth
#
# The script is used to get a detailed result from the Peripleo API.
# It takes a search term, askes for the hits and extracts all the metadata
# attached to it. The json will be transformed to geojson and exported
# into an geojson file, named after the query string.
#
# Parameters:
# -q --query= Obligatory parameter with the search term
# -l --limit= Optional parameter for limiting the result, default = 20
#
# Example:
#
# python3 getPeripleo.py -q 'province' -t 'place'

import sys, getopt
import os
import logging
import json
import requests
from urllib.parse import quote

# Function to extract all places associated with query term and receives for
# every place the full metadata and geometry
def getPeResult(peReq, query):
    placeList = []
    peRequest = requests.get(peReq).json()
    # single request for every hit, e.g. http://pelagios.org/peripleo/places/http:%2F%2Fpleiades.stoa.org%2Fplaces%2F981516?prettyprint=true
    for number in peRequest["items"]:
        print(number["identifier"])
        placeReq = "http://pelagios.org/peripleo/places/" + quote(number["identifier"], safe='')
        place = requests.get(placeReq).json()
        placeList.append(place.copy())
        json2Geojson(placeList, query)

# Function to transform json into geojson
def json2Geojson(placeList, query):
    geojson = {}
    geojson["type"] = "FeatureCollection"
    geojson["features"] = []

    for feature in placeList:
        try:
            place = {}
            place["geometry"] = feature["geometry"]
            place["properties"] = {}
            for key, value in feature.items():
                if key not in ('geometry'):
                    place["properties"][key] = value
            geojson["features"].append(place)
        except KeyError:
            print("Missing geometry!")
    with open(query + '.json', 'w') as fp:
        json.dump(geojson, fp)

# main function, for request parameter handling
def main(argv):
    query = ''
    limit = ''
    helpText = 'getPeripleo.py -q <query> [-l <limit>]'

    # request parameter handling
    try:
        opts, args = getopt.getopt(argv,"hq:l:",["query=","limit="])
    except getopt.GetoptError:
        print(helpText)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helpText)
            sys.exit()
        elif opt in ("-q", "--query"):
            query = arg
        elif opt in ("-l", "--limit"):
            limit = arg

    # build request, e.g. http://pelagios.org/peripleo/search?query=province&type=place&limit=400&prettyprint=true
    peReq = 'http://pelagios.org/peripleo/search?query=' + query + "&type=place"
    if limit != "":
        peReq = peReq + "&limit=" + limit

    print(peReq)
    getPeResult(peReq, query)

if __name__ == "__main__":
    main(sys.argv[1:])
