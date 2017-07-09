getPeripleo
=====

The script is used to get a detailed result from the Peripleo API.
It takes a search term, askes for the hits and extracts all the metadata
attached to it. The json will be transformed to geojson and exported
into an geojson file, named after the query string.

Parameters:
-----
* -q --query= Obligatory parameter with the search term
* -l --limit= Optional parameter for limiting the result, default = 20

Example:
-----
```bash
python3 getPeripleo.py -q 'province' -t 'place'
```
