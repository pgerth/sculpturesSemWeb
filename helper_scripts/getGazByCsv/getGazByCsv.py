# author: Philipp Gerth
#
# The script is used to get a RDF Output from the iDAI.gazetteer REST API
# based on the input csv file
#
# Parameters:
# -c --csv= Obligatory parameter with the csv, which contains the gaz entries
#
# Example:
#
# python3 getGazByCsv.py -c 'gaz.csv'

import sys, getopt
import os
import requests
import csv
import json
import xml.etree.ElementTree as ET


# Function to extract the correspondent iDAI.gazetteer entity
def getGazRdf(gazLink):
    gazRequest = requests.get(gazLink + '.rdf')
    #,auth=('user', 'password').json()
    print(gazRequest.text)
    f.write(str(gazRequest.text))

with open('gaz.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    f = open('myfile.rdf', 'w')
    for row in csvReader:
        print(row[0])
        getGazRdf(row[0])

    f.close()
