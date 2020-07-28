from flask import Flask, request, render_template, redirect, jsonify
# import pymysql
import os

import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

# 전국 확진자 수에 대한 시각화 지도
@app.route('/kor_defCnt_map')
def kor_defCnt_map():
    return render_template('kor_defCnt_map.html')

# 전국 사망자 수에 대한 시각화 지도
@app.route('/kor_deathCnt_map')
def kor_deathCnt_map():
    return render_template('kor_deathCnt_map.html')

# 전국 격리 해제 인원에 대한 시각화 지도
@app.route('/kor_isolClearCnt_map')
def kor_isolClearCnt_map():
    return render_template('kor_isolClearCnt_map.html')

# 시도별 발생동향 시각화 지도 및 그래프
@app.route('/cities_trend_chart')
def cities_trend_chart():
    return render_template('cities_trend_chart.html')

@app.route('/hospital_map')
def hospital_map():
    return render_template('hospital_map.html')

if __name__ == '__main__':
    app.run(debug=True, port=8089)