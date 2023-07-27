from flask import Flask, request, jsonify

app = Flask(__name__) # here app is a class name, class name, can be anything your name, my  name, etc...!

@app.route('/abc', methods=['GET','POST'])
# here GET mean posting or sending  a data with the url (or sending a data in browser in url EX: searching anything in the Google search bar)
# here POST means posting or sending the data with the bodY  (body means  encrypted one, like not showing username or password in that  particular link, EX: any account username and password)
def test1():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/test2',methods=['GET','POST'])
def test2():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc1/naveen/test3',methods=['GET','POST'])
def test3():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify((str(result)))

@app.route('/abc/naveen/test4',methods=['GET','POST'])
def test4():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify((str(result)))

@app.route('/abc1/naveen/test5',methods=['GET','POST'])
def test5():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a-b
        return jsonify((str(result)))

@app.route('/abc1/naveen/test6',methods=['GET','POST'])
def test6():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify((str(result)))

@app.route('/abc1/naveen/test7',methods=['GET','POST'])
def test7():
    if(request.method == 'POST'):  # again request is the class,by which we can  call different, different method inside the class.
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()



