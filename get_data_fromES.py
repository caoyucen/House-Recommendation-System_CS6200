import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch


if __name__ == '__main__':
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_index2"
    # _search_area = "UniqId"
    # _search_data = "81783dcb052b15e3b435b84250a9b405"
    _search_area = "Description"
    _search_data = "Fireplace"
    # res = es.search(index=_index, body={"query": {"match": {_search_area: _search_data}}})
    res = es.search(index=_index, body={"query": {"match": {"Description": "Fireplace"}}})
    # res = es.search(index=_index, body=
    # {
    #     "query": {
    #         "multi_match": {
    #             "State": "CA",
    #             "Zipcode": "94070"
    #         }
    #     }
    # }
        # {
        #     "query":{
        #         "filtered":{
        #             "filter":{
        #                 "bool":{
        #                     "must":[{
        #                         "match": {_search_area: _search_data}}
        #                         ]
        #                     }
        #                 }
        #             }
        #         }
        #     }
        #  )
    print(res)