from flask import Flask,render_template,request
from flask_mail import Mail,Message
import json
import requests

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="divyacf4@gmail.com"
app.config['MAIL_PASSWORD']="D!vya"

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
        message=Message("Hello! This is a mail from "+ email+" regarding the Contact us form ",sender="divyacf4@gmail.com",recipients=["divyacf4@gmail.com"])
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
    with open(r"static/json/maharashtra.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/maharashtra")
def maharashtra():
    data=requests.get("http://127.0.0.1:5312/maharashtra_api")
    data=json.loads(data.content)
    return render_template("maharashtra.html", data=data)

@app.route("/uttarpradesh_api")
def uttarpradesh_api():
    with open(r"static/json/uttarpradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/uttarpradesh")
def uttarpradesh():
    data=requests.get("http://127.0.0.1:5312/uttarpradesh_api")
    data=json.loads(data.content)
    return render_template("uttarpradesh.html", data=data)

@app.route("/andhrapradesh_api")
def andhrapradesh_api():
    with open(r"static/json/andhrapradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/andhrapradesh")
def andhrapradesh():
    data=requests.get("http://127.0.0.1:5312/andhrapradesh_api")
    data=json.loads(data.content)
    return render_template("andhrapradesh.html", data=data)

@app.route("/telangana_api")
def telangana_api():
    with open(r"static/json/telangana.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/telangana")
def telangana():
    data=requests.get("http://127.0.0.1:5312/telangana_api")
    data=json.loads(data.content)
    return render_template("telangana.html", data=data)

@app.route("/tamilnadu_api")
def tamilnadu_api():
    with open(r"static/json/tamilnadu.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/tamilnadu")
def tamilnadu():
    data=requests.get("http://127.0.0.1:5312/tamilnadu_api")
    data=json.loads(data.content)
    return render_template("tamilnadu.html", data=data)

@app.route("/kerala_api")
def kerala_api():
    with open(r"static/json/kerala.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/kerala")
def kerala():
    data=requests.get("http://127.0.0.1:5312/kerala_api")
    data=json.loads(data.content)
    return render_template("kerala.html", data=data)

@app.route("/karnataka_api")
def karnataka_api():
    with open(r"static/json/karnataka.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/karnataka")
def karnataka():
    data=requests.get("http://127.0.0.1:5312/karnataka_api")
    data=json.loads(data.content)
    return render_template("karnataka.html", data=data)

@app.route("/punjab_api")
def punjab_api():
    with open(r"static/json/punjab.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/punjab")
def punjab():
    data=requests.get("http://127.0.0.1:5312/punjab_api")
    data=json.loads(data.content)
    return render_template("punjab.html", data=data)

@app.route("/gujarat_api")
def gujarat_api():
    with open(r"static/json/gujarat.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/gujarat")
def gujarat():
    data=requests.get("http://127.0.0.1:5312/gujarat_api")
    data=json.loads(data.content)
    return render_template("gujarat.html", data=data)

@app.route("/madhyapradesh_api")
def madhyapradesh_api():
    with open(r"static/json/madhyapradesh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/madhyapradesh")
def madhyapradesh():
    data=requests.get("http://127.0.0.1:5312/madhyapradesh_api")
    data=json.loads(data.content)
    return render_template("madhyapradesh.html", data=data)

@app.route("/haryana_api")
def haryana_api():
    with open(r"static/json/haryana.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/haryana")
def haryana():
    data=requests.get("http://127.0.0.1:5312/haryana_api")
    data=json.loads(data.content)
    return render_template("haryana.html", data=data)

@app.route("/monuments_api")
def monuments_api():
    with open(r"static/json/monuments.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/monuments")
def monuments():
    data=requests.get("http://127.0.0.1:5312/monuments_api")
    data=json.loads(data.content)
    return render_template("monuments.html", data=data)

@app.route("/indianfood_api")
def indianfood_api():
    with open(r"static/json/indianfood.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/indianfood")
def indianfood():
    data=requests.get("http://127.0.0.1:5312/indianfood_api")
    data=json.loads(data.content)
    return render_template("indianfood.html", data=data)

@app.route("/culture_api")
def culture_api():
    with open(r"static/json/culture.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/culture")
def culture():
    data=requests.get("http://127.0.0.1:5312/culture_api")
    data=json.loads(data.content)
    return render_template("culture.html", data=data)

@app.route("/language_api")
def language_api():
    with open(r"static/json/language.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/language")
def language():
    data=requests.get("http://127.0.0.1:5312/language_api")
    data=json.loads(data.content)
    return render_template("language.html", data=data)

@app.route("/music_api")
def music_api():
    with open(r"static/json/music.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/music")
def music():
    data=requests.get("http://127.0.0.1:5312/music_api")
    data=json.loads(data.content)
    return render_template("music.html", data=data)

@app.route("/dance_api")
def dance_api():
    with open(r"static/json/dance.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/dance")
def dance():
    data=requests.get("http://127.0.0.1:5312/dance_api")
    data=json.loads(data.content)
    return render_template("dance.html", data=data)

@app.route("/himachal_api")
def himachal_api():
    with open(r"static/json/himachal.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/himachal")
def himachal():
    data=requests.get("http://127.0.0.1:5312/himachal_api")
    data=json.loads(data.content)
    return render_template("himachal.html", data=data)

@app.route("/bengal_api")
def bengal_api():
    with open(r"static/json/bengal.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/bengal")
def bengal():
    data=requests.get("http://127.0.0.1:5312/bengal_api")
    data=json.loads(data.content)
    return render_template("bengal.html", data=data)

@app.route("/bihar_api")
def bihar_api():
    with open(r"static/json/bihar.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/bihar")
def bihar():
    data=requests.get("http://127.0.0.1:5312/bihar_api")
    data=json.loads(data.content)
    return render_template("bihar.html", data=data)

@app.route("/chhatisgarh_api")
def chhatisgarh_api():
    with open(r"static/json/chhatisgarh.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/chhatisgarh")
def chhatisgarh():
    data=requests.get("http://127.0.0.1:5312/chhatisgarh_api")
    data=json.loads(data.content)
    return render_template("chhatisgarh.html", data=data)

@app.route("/jharkhand_api")
def jharkhand_api():
    with open(r"static/json/jharkhand.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/jharkhand")
def jharkhand():
    data=requests.get("http://127.0.0.1:5312/jharkhand_api")
    data=json.loads(data.content)
    return render_template("jharkhand.html", data=data)

@app.route("/odisha_api")
def odisha_api():
    with open(r"static/json/odisha.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/odisha")
def odisha():
    data=requests.get("http://127.0.0.1:5312/odisha_api")
    data=json.loads(data.content)
    return render_template("odisha.html", data=data)

@app.route("/sikkim_api")
def sikkim_api():
    with open(r"static/json/sikkim.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/sikkim")
def sikkim():
    data=requests.get("http://127.0.0.1:5312/sikkim_api")
    data=json.loads(data.content)
    return render_template("sikkim.html", data=data)

@app.route("/uttarakhand_api")
def uttarakhand_api():
    with open(r"static/json/uttarakhand.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/uttarakhand")
def uttarakhand():
    data=requests.get("http://127.0.0.1:5312/uttarakhand_api")
    data=json.loads(data.content)
    return render_template("uttarakhand.html", data=data)


@app.route("/meghalaya_api")
def meghalaya_api():
    with open(r"static/json/meghalaya.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/meghalaya")
def meghalaya():
    data=requests.get("http://127.0.0.1:5312/meghalaya_api")
    data=json.loads(data.content)
    return render_template("meghalaya.html", data=data)


@app.route("/tripura_api")
def tripura_api():
    with open(r"static/json/tripura.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/tripura")
def tripura():
    data=requests.get("http://127.0.0.1:5312/tripura_api")
    data=json.loads(data.content)
    return render_template("tripura.html", data=data)


@app.route("/arunachal_api")
def arunachal_api():
    with open(r"static/json/arunachal.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/arunachal")
def arunachal():
    data=requests.get("http://127.0.0.1:5312/arunachal_api")
    data=json.loads(data.content)
    return render_template("arunachal.html", data=data)

@app.route("/assam_api")
def assam_api():
    with open(r"static/json/assam.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/assam")
def assam():
    data=requests.get("http://127.0.0.1:5312/assam_api")
    data=json.loads(data.content)
    return render_template("assam.html", data=data)


@app.route("/manipur_api")
def manipur_api():
    with open(r"static/json/manipur.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/manipur")
def manipur():
    data=requests.get("http://127.0.0.1:5312/manipur_api")
    data=json.loads(data.content)
    return render_template("manipur.html", data=data)


@app.route("/nagaland_api")
def nagaland_api():
    with open(r"static/json/nagaland.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/nagaland")
def nagaland():
    data=requests.get("http://127.0.0.1:5312/nagaland_api")
    data=json.loads(data.content)
    return render_template("nagaland.html", data=data)

@app.route("/mizoram_api")
def mizoram_api():
    with open(r"static/json/mizoram.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/mizoram")
def mizoram():
    data=requests.get("http://127.0.0.1:5312/mizoram_api")
    data=json.loads(data.content)
    return render_template("mizoram.html", data=data)

@app.route("/jammu_api")
def jammu_api():
    with open(r"static/json/jammu.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/jammu")
def jammu():
    data=requests.get("http://127.0.0.1:5312/jammu_api")
    data=json.loads(data.content)
    return render_template("jammu.html", data=data)

@app.route("/greatest_api")
def greatest_api():
    with open(r"static/json/greatest.json",'r') as jsonfile:
        data=json.loads(jsonfile.read())
    return data

@app.route("/greatest")
def greatest():
    data=requests.get("http://127.0.0.1:5312/greatest_api")
    data=json.loads(data.content)
    return render_template("greatest.html", data=data)


if __name__=="__main__":
    app.run(debug=True,port=5312)
