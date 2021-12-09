import urllib

import simplejson as json
from flask import Flask, render_template, request
from flask import request
from elasticsearch import Elasticsearch
from urllib.error import HTTPError

es = Elasticsearch(host="localhost", port=9200)
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/personal', methods=['GET', 'POST'])
def get_result():
    print("COME TO THE personal PAGE!!!!")
    _search_area = "Description"
    _search_data = "like"
    _index = "test_project_index2"
    res = es.search(index=_index, body={"query": {"match": {_search_area: _search_data}}})
    #print(res)
    allDatas = res.get("hits").get("hits")
    # print("allDatas =")
    # print(allDatas)
    #jsonString = str(json.dumps(allDatas)).replace("\"", "'")
    # print("jsonString = ")
    # print(jsonString)
    dataList = []
    count = 0
    for data in allDatas:
        print(type(data))
        # print("data = ")
        # print(data)
        newString = data['_source']['Description']
        imgUrl = data['_source']['ImageUrl']

        try:
            urllib.request.urlretrieve(imgUrl)
        except urllib.error.HTTPError as err:
            print("err code = ")
            print(err.code)
            data['_source'][
                'ImageUrl'] = "https://static.trulia-cdn.com/pictures/thumbs_5/ps.115/f/1/9/e/picture-uh=50a3fff10b8c3a0e1a30fa26a4b5f8-ps=f19eee5cfe208912d924bf9136f63c66.jpg"
        data['_source']['Description'] = str(newString).replace("\"", " ")
        dataList.append(data['_source'])
        count = count + 1
    print(count)
    jsonString = str(json.dumps(dataList)).replace("'", " ")
    #jsonString = json.dumps(dataList)
    print(jsonString)
    # #print(dataList)
    # jsonString = json.dumps(dataList)
    #print(jsonString)
    return render_template('personal_mainPage.html', Datas=jsonString)


if __name__ == '__main__':
    app.run(debug=True)
