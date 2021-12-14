import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch


def check_houseData():
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_index2"
    # _search_area = "UniqId"
    # _search_data = "81783dcb052b15e3b435b84250a9b405"
    _search_area = "Description"
    _search_data = "Fireplace"
    UniqId = "4bdd7a810e393f20de4392a9e46165f3"
    # res = es.search(index=_index, body={"query": {"match": {_search_area: _search_data}}})
    res = es.search(index=_index, size=20, body={"query": {"match": {"Description": "Fireplace"}}})
    # res = es.search(index=_index, body={"query": {"match": {"UniqId": UniqId}}})
    print(res)

def check_userData(name):
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_user1"
    name = name
    res = es.search(index=_index, body={"query": {"match": {"name": name}}})
    print(res)

def update_userData(name, newString):
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_user1"
    res = es.search(index=_index, body={"query": {"match": {"name": name}}})
    data = res.get("hits").get("hits")
    # print(data[0])
    userDate = data[0].get("_source")
    new = userDate.get("allHistory") + " " + newString
    userDate["allHistory"] = new
    # print(userDate)
    # print(data[0].get("_index"))
    # print(data[0].get("_type"))
    # print(data[0].get("_id"))
    # udata = {}
    # udata["doc"] = userDate
    # print(udata)
    es.update(index=_index, id=data[0].get("_id"), body={'doc': userDate})



if __name__ == '__main__':
    # check_houseData()
    check_userData("amy")
    #update_userData("YYDS", "fire")