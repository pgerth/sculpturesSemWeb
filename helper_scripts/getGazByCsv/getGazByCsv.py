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
def getGazRdf(gazLink, f):
    gazRequest = requests.get(gazLink + '.rdf')
    #,auth=('user', 'password').json()
    print(gazRequest.text)
    f.write(str(gazRequest.text))

# main function, for request parameter handling
def main(argv):
    gazCsv = 'gaz.csv'
    export = 'export.rdf'
    helpText = 'getGazByCsv.py -c <csv> [-e <export>]'

    # request parameter handling
    try:
        opts, args = getopt.getopt(argv,"hc:e:",["query=","export="])
    except getopt.GetoptError:
        print(helpText)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helpText)
            sys.exit()
        elif opt in ("-c", "--csvfile"):
            gazCsv = arg
        elif opt in ("-e", "--export"):
            export = arg


    with open(gazCsv, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        f = open(export, 'w')
        for row in csvReader:
            print(row[0])
            getGazRdf(row[0], f)

        f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
