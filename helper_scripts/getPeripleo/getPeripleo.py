# author: Philipp Gerth
#
# The script is used to get a detailed result from the Peripleo API.
# It takes a search term, askes for the hits and extracts all the metadata
# attached to it.
#
# Parameters:
# -q --query= Obligatory parameter with the search term
# -t --type= Optional parameter for limiting the result to a specific type:
#  place, item, dataset
#
# Example:
#
# python getPeripleo.py -q 'province' -t 'place/'

import sys, getopt
import requests
import csv
import json


# Function to extract all entrys associated with provinces
def getPeResult(peReq):
    peRequest = requests.get(peReq)
    print(peRequest)
    f.write(str(peRequest.json))

def main(argv):
    query = ''
    qType = ''
    helpText = 'getPeripleo.py -q <query> [-t <type>]'

    try:
        opts, args = getopt.getopt(argv,"hq:t:",["query=","type="])
    except getopt.GetoptError:
        print helpText
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print helpText
            sys.exit()
        elif opt in ("-q", "--query"):
            query = arg
        elif opt in ("-t", "--type"):
            qType = arg

    if csvFile != "":
        print 'Csv input file is: ', csvFile
        createFileDict(targetDir, fileType, fileDict)
        metadataByCsv(csvFile, targetDir, fileDict)
