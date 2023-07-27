# API (Application programming interface)

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/abc', methods = ['GET','POST'])
def test1():
    if (request.method == 'POST'):
        a = request.json['number1']
        b = request.json['number2']
        result = a+b
        return jsonify((str(result)))


@app.route('/abcd1/naveen',methods= ['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['number1']
        b = request.json['number2']
        result = a*b

        return jsonify(str(result))

@app.route('/abcdef/naveen',method =['GET',"POST"])
def test3():
    if (request.method == 'POST'):
        a = request.json['number1']
        b = request.json['number2']
        result = a/b
        return jsonify((str(result )))

@app.route('abcd/naveen/adep', method = [ 'GET','POST'])
def test4():
    if (request.method=='POST'):
        a = request.json["number1"]
        b = request.json["number2"]
        result = a%b
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()

"""
def test(a,b):
    return a+b

print(test(4,5))
"""





