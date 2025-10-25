# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 08:33:07 2025

@author: Manoj Eregowda
"""

# app.py
from flask import Flask, request

# ✅ Import the function from multi.py
from multi import multiplication_table

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <center>
    <body style="background-color:powderblue;"> ​ 
    <h2>Multiplication Table Generator</h2>
    <form action="/result" method="post">
        Enter a number: <input type="text" name="num">
        <input type="submit" value="Generate">
    </form>
    </center>
    '''

@app.route('/result', methods=['POST'])
def result():
    num = int(request.form['num'])
    table = multiplication_table(num)
    # Convert list into HTML-friendly format
    html_result = "<br>".join(table)
    return f"<h2>Multiplication Table for {num}</h2><p>{html_result}</p>"

if __name__ == '__main__':
    app.run()
