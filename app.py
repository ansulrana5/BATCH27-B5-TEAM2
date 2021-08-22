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

@app.route("/andhrapradesh_api")
def andhrapradesh_api():
    with open(r"andhrapradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/andhrapradesh")
def andhrapradesh():
    data=requests.get("http://127.0.0.1:5312/andhrapradesh_api")
    data=json.loads(data.content)
    return render_template("andhrapradesh.html", data=data)

@app.route("/telangana_api")
def telangana_api():
    with open(r"telangana.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/telangana")
def telangana():
    data=requests.get("http://127.0.0.1:5312/telangana_api")
    data=json.loads(data.content)
    return render_template("telangana.html", data=data)

@app.route("/tamilnadu_api")
def tamilnadu_api():
    with open(r"tamilnadu.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/tamilnadu")
def tamilnadu():
    data=requests.get("http://127.0.0.1:5312/tamilnadu_api")
    data=json.loads(data.content)
    return render_template("tamilnadu.html", data=data)

@app.route("/kerala_api")
def kerala_api():
    with open(r"kerala.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/kerala")
def kerala():
    data=requests.get("http://127.0.0.1:5312/kerala_api")
    data=json.loads(data.content)
    return render_template("kerala.html", data=data)

@app.route("/karnataka_api")
def karnataka_api():
    with open(r"karnataka.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/karnataka")
def karnataka():
    data=requests.get("http://127.0.0.1:5312/karnataka_api")
    data=json.loads(data.content)
    return render_template("karnataka.html", data=data)

@app.route("/punjab_api")
def punjab_api():
    with open(r"punjab.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/punjab")
def punjab():
    data=requests.get("http://127.0.0.1:5312/punjab_api")
    data=json.loads(data.content)
    return render_template("punjab.html", data=data)

@app.route("/gujarat_api")
def gujarat_api():
    with open(r"gujarat.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/gujarat")
def gujarat():
    data=requests.get("http://127.0.0.1:5312/gujarat_api")
    data=json.loads(data.content)
    return render_template("gujarat.html", data=data)

@app.route("/madhyapradesh_api")
def madhyapradesh_api():
    with open(r"madhyapradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/madhyapradesh")
def madhyapradesh():
    data=requests.get("http://127.0.0.1:5312/madhyapradesh_api")
    data=json.loads(data.content)
    return render_template("madhyapradesh.html", data=data)

@app.route("/haryana_api")
def haryana_api():
    with open(r"haryana.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/haryana")
def haryana():
    data=requests.get("http://127.0.0.1:5312/haryana_api")
    data=json.loads(data.content)
    return render_template("haryana.html", data=data)


if __name__=="__main__":
    app.run(debug=True,port=5312)
