from SPARQLWrapper import SPARQLWrapper, JSON
import requests

# Query to the British Museum SPARQL endpoint
# The query asks for all places, that are countries or city states (place type c)
sparql = SPARQLWrapper("http://collection.britishmuseum.org/sparql")
sparql.setQuery("""
    PREFIX crm: <http://erlangen-crm.org/current/>
    PREFIX fts: <http://www.ontotext.com/owlim/fts#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX thes: <http://collection.britishmuseum.org/id/thesauri/>

    SELECT DISTINCT ?place ?label
    WHERE { 
        ?place skos:prefLabel ?label .     
        ?place crm:P2_has_type <http://collection.britishmuseum.org/id/place/type/C> .
    }
    LIMIT 1
""")
# Defines the output format of the SPARQL endpoint: JSON
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Function to extract the correspondent iDAI.gazetteer entity 
def gazLink(bmLabel):
    gazResponse = requests.get('https://gazetteer.dainst.org/search.json?q='+result["label"]["value"]).json()
    #,auth=('user', 'password').json()
    return gazResponse[]

for result in results["results"]["bindings"]:
    print(result["label"]["value"])
    print(result["place"]["value"])
    gaz = gazLink(result["label"]["value"])
    print(gaz)
