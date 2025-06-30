from flask import Flask, render_template, request, redirect
import numpy as np

app = Flask(__name__)
app.secret_key = "pakka fail in EM"

@app.route('/')
def home():
    return render_template('home.html')

app.run(debug=True)