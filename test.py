from flask import request,jsonify
from flask import Flask, render_template,url_for
import requests
import json

app=Flask(__name__)
@app.route('/')
@app.route('/getWeather')
def getweather():
	return render_template('test.html')

@app.route('/get_city_weather',methods=['POST'])
def getCurrentWeather():
	city=request.form['cityname']
	key="your appid from openweathermap"  # like eg.  key="k123124993294nkjk123"
	headers={'Accept':'identity'}
	content=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+key).json()
	return json.dumps(content["weather"][0]["description"])

if __name__=='__main__':
	app.run(debug=True)