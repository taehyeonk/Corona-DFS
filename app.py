from flask import Flask, request, render_template, redirect, jsonify
import pymysql
import os

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8089)