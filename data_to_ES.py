import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch

if __name__ == '__main__':
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch()
    _index = "test_project_index2"
    i = 0
    with open('data.json') as raw_data:
        json_docs = json.load(raw_data)
        for json_doc in json_docs:
            # print(json_doc)
            i = i + 1
            es.index(index=_index, document=json.dumps(json_doc))
            print(i)

    # http://localhost:9200/test_project_index1/_search
    # http://localhost:9200/test_project_index1/_search?q=UniqId:81783dcb052b15e3b435b84250a9b405









