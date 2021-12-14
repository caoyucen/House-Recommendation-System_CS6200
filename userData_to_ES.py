import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch


    # http://localhost:9200/test_project_user/_search
    # http://localhost:9200/test_project_user/_search?q=UniqId:81783dcb052b15e3b435b84250a9b405

if __name__ == '__main__':
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch()
    _index = "test_project_user"
    userName = ["Liu", "Cao", "Li", "Wang"]
    users = {}
    for name in userName:
        user = {}
        user["name"] = name
        user["income"] = 123,000
        user["allHistory"] = "school"
        users[name] = user
        es.index(index=_index, document=json.dumps(user))











