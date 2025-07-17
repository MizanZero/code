from flask import Flask, render_template, redirect, session
import sqlite3 as sq

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)