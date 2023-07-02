from flask import Flask, render_template, request, session, url_for, redirect, flash
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chaitu26c"
cluster = MongoClient("mongodb+srv://chaitu26c:umaidoughnut26c%40mongo.com@cluster0.8fdj3ck.mongodb.net/?retryWrites=true&w=majority")
db = cluster["new"]
collection = db["new"]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login_form', methods=['POST','GET'])
def login():
    username=request.form['username']
    password=request.form['password']
    data = collection.find_one({"email": username, "password": password})
    if data!=None:
            return render_template('account.html', welcomename = username)
    else:
        return redirect(url_for('newaccount'))


@app.route('/signup_form', methods=['POST','GET'])
def signup():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    conformpassword=request.form['conformpassword']
    tandc=request.form.get("tandc")
    if password==conformpassword:
        collection.insert_one({
            "name": name,
            "email": email,
            "password": conformpassword,
            "date_time": datetime.utcnow()
        })
        return render_template('account.html', welcomename = name)

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/newaccount')
def newaccount():
    return render_template('newaccount.html')

if __name__ == '__main__':
    app.run(debug=True)
