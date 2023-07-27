from flask import Flask, request,jsonify
import pymongo

app =  Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Naveen_ineuron:Harekrishna123@cluster0.vzehpr8.mongodb.net/?retryWrites=true&w=majority")
db = client['mysqltable']
collection = db['taskcollection']

@app.route("/insert/mongo",methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("succefully inserted"))


if __name__ =='__main__':
    app.run(port=5001)
