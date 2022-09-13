
from flask import Flask,jsonify,render_template,request

app=Flask(__name__)  #creating a object to contain data
@app.route('/Gayathri')
def check():
	return "Good Evening everyone,Lets dive into first application using Flask"

a=[1,2,3,4,5]  #if we give a tuple also for jsonfiy it is stored as list only
@app.route('/sampledata')  #after route statement it should always be a function
def printdata():
	return jsonify(a)

@app.route('/basic')
def greet():
	return render_template('index.html')

mydata=[{'id':1,'name':'Gayathri','quote':'Enthusiastic Person'},
        {'id':2,'name':'Bhavana','quote':'Leadership Qualities'},
		{'id':3,'name':'Hafsa','quote':'Smart Thinking'}]
@app.route('/data',methods=['GET'])  #implicitely method is always get
def new():
	return jsonify(mydata)    #for us it is list,for web it is json,data.text gives as string

@app.route('/adddata',methods=['POST'])  #endpoint
def addData():
	data=request.get_json()
	inc=mydata[-1]['id']+1
	data['id']=inc
	mydata.append(data)
	return jsonify(mydata)
#update ,we take which id I want to update
@app.route('/update/<int:id>',methods=['PUT'])
def updateData(id):
	data=request.get_json()
	for i in mydata:
		print(i['id'])
		if i['id']==id:
			i['name']=data['name'] #only updating the name
	return jsonify(mydata)

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
	for i in mydata:
		if i['id']==id:
			mydata.remove(i)
	return jsonify(mydata)
app.run()


