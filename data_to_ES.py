import simplejson as json
import json
import csv
from elasticsearch import Elasticsearch



    # Read a XML file with <RECORD> as tag for each document
    # """
    #
    # # _DOC_DELIMITER_TAG = "RECORD"
    #
    # def __init__(self, id_offset=0):
    #     self.id_offset = id_offset
    #
    # def _read_xml_as_dicts(self, xml_fp):
    #     xml = xml_fp.read()
    #     xml_dicts = xmltodict.parse(xml)
    #     json.dumps(xml_dicts)
    #     return xml_dicts


    # http://localhost:9200/test_project_index1/_search
    # http://localhost:9200/test_project_index1/_search?q=UniqId:81783dcb052b15e3b435b84250a9b405

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










