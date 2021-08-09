from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/Map")
def Map():
    return render_template('map.html')

@app.route("/About")
def About():
    return render_template('about.html')

@app.route("/Contact")
def Contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True,port=5312)
