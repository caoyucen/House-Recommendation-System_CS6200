import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch

if __name__ == '__main__':
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch()
    _index = "test_project_user1"
    userName = ["Tom", "caoyucen", "amy", "Jack"]
    tempString = ["fireplace", "school", "storage", "designer"]
    users = {}
    i = 0
    for name in userName:
        user = {}
        user["name"] = name
        user["income"] = 123,000
        user["allHistory"] = tempString[i]
        users[name] = user
        i = i + 1
        es.index(index=_index, document=json.dumps(user))



    # http://localhost:9200/test_project_user1/_search








