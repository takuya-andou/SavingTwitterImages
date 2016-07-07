# -*- coding: utf-8 -*-
#!/usr/bin/env python2
import json
import os
import tempfile
import pymongo

# pip install flask
from flask import Flask, request, make_response, abort, render_template  

# mongodb へのアクセスを確立
client = pymongo.MongoClient('localhost', 27017)
# データベースを作成 (名前: my_database)
db = client.my_database
# コレクションを作成 (名前: my_collection)
co = db.my_collection

# Flask Settings
DEBUG = True
UPLOAD_FOLDER = "tmp"
MODEL_FOLDER = "model"
SUPPORT_EXTENSIONS = set([".jpg", ".jpeg", ".png"])
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def help():
	html=""
	for data in co.find({},{ "_id": 0 }).sort("_id", -1).limit(10):
		#temp_data = json.dumps(data)
		#print type(temp_data)
		tmp_data = data.values()
		html=str(html)+'<a href="https://twitter.com/'+str(tmp_data[2])+'"><img width="100px" src="'+str(tmp_data[0])+'">'+'<BR>'
	return render_template('index.html',html=html)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,processes=3)
