from flask import Flask, request, render_template, redirect, jsonify
# import pymysql
import os

import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

import requests
from datetime import datetime

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

# 선별진료소 시각화 지도
@app.route('/hospital_map')
def hospital_map():
    return render_template('hospital_map.html')

# 코로나19 관련 뉴스 크롤링
@app.route('/news')
def news():
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코로나19",headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.type01 > li")
    time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    newslist=[]
    
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist.append(dic)
        
    return render_template('news.html',newslist = newslist,time=time)

if __name__ == '__main__':
    app.run(debug=True, port=8089)


