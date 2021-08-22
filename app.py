from flask import Flask,render_template,request
from flask_mail import Mail,Message
import json
import requests

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="xyz@gmail.com"
app.config['MAIL_PASSWORD']="123456789"

mail=Mail(app)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/Map")
def Map():
    return render_template('map.html')

@app.route("/About")
def About():
    return render_template('about.html')

@app.route("/Contact",methods=['GET','POST'])
def Contact():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        msg=request.form['subject']
        message=Message("Hello! This is a mail from "+ email+" regarding the Contact us form ",sender="xyz@gmail.com",recipients=["rana5312ansul@gmail.com"])
        message.body=msg
        mail.send(message)   
    return render_template('contact.html')

@app.route("/Team")
def Team():
    return render_template('team.html')

@app.route("/Gallery")
def Gallery():
    return render_template('art.html')

@app.route("/maharashtra_api")
def maharashtra_api():
    with open(r"maharashtra.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/maharashtra")
def maharashtra():
    data=requests.get("http://127.0.0.1:5312/maharashtra_api")
    data=json.loads(data.content)
    return render_template("maharashtra.html", data=data)

@app.route("/uttarpradesh_api")
def uttarpradesh_api():
    with open(r"uttarpradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/uttarpradesh")
def uttarpradesh():
    data=requests.get("http://127.0.0.1:5312/uttarpradesh_api")
    data=json.loads(data.content)
    return render_template("uttarpradesh.html", data=data)

if __name__=="__main__":
    app.run(debug=True,port=5312)
