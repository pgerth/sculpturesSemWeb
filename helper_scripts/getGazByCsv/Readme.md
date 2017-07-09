getGazByCsv
=====

The script is used to get a RDF Output from the iDAI.gazetteer REST API
based on the input csv file

Parameters:
-----
* -c --csv= Obligatory parameter with the csv, which contains the gaz entries
* -e --export= Optional parameter for limiting the result, default = 20

Example:
-----
```bash
python3 getGazByCsv.py -c 'gaz.csv'
```
