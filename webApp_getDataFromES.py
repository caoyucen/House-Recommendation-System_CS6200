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
def get_personalResult():
    username = request.form.get("username")
    print("!!!!username =")
    print(username)
    _search_data = ""
    if(username):
        _search_data = get_userData(username)
    if(len(_search_data) == 0):
        _search_data = "like"
    print("_search_data =")
    print(_search_data)
    _search_area = "Description"
    _index = "test_project_index2"
    res = es.search(index=_index, size=20, body={"query": {"match": {_search_area: _search_data}}})
    allDatas = res.get("hits").get("hits")
    dataList = []
    count = 0
    for data in allDatas:
        # print(type(data))
        newString = data['_source']['Description']
        imgUrl = data['_source']['ImageUrl']
        if (imgUrl == ""):
            data['_source'][
                'ImageUrl'] = "https://static.trulia-cdn.com/pictures/thumbs_5/ps.115/f/1/9/e/picture-uh=50a3fff10b8c3a0e1a30fa26a4b5f8-ps=f19eee5cfe208912d924bf9136f63c66.jpg"
        else:
            try:
                urllib.request.urlretrieve(imgUrl)
            except urllib.error.HTTPError as err:
                # print("err code = ")
                # print(err.code)
                data['_source'][
                    'ImageUrl'] = "https://static.trulia-cdn.com/pictures/thumbs_5/ps.115/f/1/9/e/picture-uh=50a3fff10b8c3a0e1a30fa26a4b5f8-ps=f19eee5cfe208912d924bf9136f63c66.jpg"
        data['_source']['Description'] = str(newString).replace("\"", " ")
        dataList.append(data['_source'])
        count = count + 1
    print(count)
    jsonString = str(json.dumps(dataList)).replace("'", " ")
    return render_template('personal_mainPage.html', Datas=jsonString, UserName=username)


@app.route('/searchResult', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        print("COME TO THE PAGE!!!!")
        _search_area = request.form.get("searchArea")
        _search_data = request.form.get("searchWord")
        _user_name = request.form.get("userName")
        print("_user_name =")
        print(_user_name)
        update_userData(_user_name, _search_data)
        _index = "test_project_index2"
        res = es.search(index=_index, size=20,  body={"query": {"match": {_search_area: _search_data}}})
        allDatas = res.get("hits").get("hits")
        dataList = []
        count = 0
        for data in allDatas:
            # print(type(data))
            newString = data['_source']['Description']
            imgUrl = data['_source']['ImageUrl']
            if(imgUrl == ""):
                data['_source'][
                    'ImageUrl'] = "https://static.trulia-cdn.com/pictures/thumbs_5/ps.115/f/1/9/e/picture-uh=50a3fff10b8c3a0e1a30fa26a4b5f8-ps=f19eee5cfe208912d924bf9136f63c66.jpg"
            else:
                try:
                    urllib.request.urlretrieve(imgUrl)
                except urllib.error.HTTPError as err:
                    # print("err code = ")
                    # print(err.code)
                    data['_source'][
                    'ImageUrl'] = "https://static.trulia-cdn.com/pictures/thumbs_5/ps.115/f/1/9/e/picture-uh=50a3fff10b8c3a0e1a30fa26a4b5f8-ps=f19eee5cfe208912d924bf9136f63c66.jpg"
            data['_source']['Description'] = str(newString).replace("\"", " ")
            dataList.append(data['_source'])
            count = count + 1
        print(count)
        jsonString = str(json.dumps(dataList)).replace("'", " ")
        # print(jsonString)
        return render_template('searchResultPage.html', Datas=jsonString)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    print("login ")
    return render_template('login.html')


def get_userData(name):
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_user1"
    res = es.search(index=_index, body={"query": {"match": {"name": name}}})
    # print(res)
    data = res.get("hits").get("hits")
    # print(data)
    if(len(data) < 1):
        return ""
    return data[0].get("_source").get("allHistory")

def update_userData(name, addString):
    es = Elasticsearch(host="localhost", port=9200)
    _index = "test_project_user1"
    res = es.search(index=_index, body={"query": {"match": {"name": name}}})
    data = res.get("hits").get("hits")
    userDate = data[0].get("_source")
    newString = addString + " " + userDate.get("allHistory")
    userDate["allHistory"] = newString
    es.update(index=_index, id=data[0].get("_id"), body={'doc': userDate})

if __name__ == '__main__':
    app.run(debug=True)
