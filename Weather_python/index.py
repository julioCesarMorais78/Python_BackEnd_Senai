import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def weather():
	url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
	#querystring = {"lat":"-23.55052","lon":"-46.633308","date":"2021-08-24","units":"auto"}
	querystring = {"text":"Sao Paulo","language":"pt"}
 
	headers = {
		"x-rapidapi-key": "3cf527f877mshf7cdb40726a82c0p1512a5jsn7d6b8b198527",
		"x-rapidapi-host": "ai-weather-by-meteosource.p.rapidapi.com"
	}
	response = requests.get(url, headers=headers, params=querystring)
	return jsonify(response.json())

if __name__ == '__main__':
	app.run(debug=True)