#from SPARQLWrapper import SPARQLWrapper, JSON
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

'''
for result in results["results"]["bindings"]:
    print(result["label"]["value"])
    print(result["place"]["value"])
    gaz = gazLink(result["label"]["value"])
    print(gaz)
'''
