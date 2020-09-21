from flask import Flask, request
import json
import requests
import random

app = Flask('bootcamp')

@app.route('/movie', methods=['GET', 'POST'])
def findMovie():
  moviestar = request.values['Body']

  response = requests.get("https://api.themoviedb.org/3/search/person", params={
    'api_key':'f3fcd2402f0ff4736d01d69bf60715d7',
    'query':moviestar
  })
  data = json.loads(response.content)
  if len(data['results'])== 0: return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>Is that a real actor name?! Give me an actor name!</Message>
  </Response>"""
  star = data['results'][0]['name']
  starId = data['results'][0]['id']
  response = requests.get("https://api.themoviedb.org/3/discover/movie", params={
    'api_key':'f3fcd2402f0ff4736d01d69bf60715d7',
    'with_people':starId
  })
  data = json.loads(response.content)
  resultsCount = len(data['results'])
  randNum = random.randint(1,resultsCount) - 1
  movie = data['results'][randNum]['original_title']
  poster = data['results'][randNum]['poster_path']
  return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>My pick for you is... {}<Media>https://image.tmdb.org/t/p/w1280{}</Media></Message></Response>'.format(movie, poster)

@app.route('/sms', methods=['GET', 'POST'])
def sms():
  return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>Hello from Bootcamp!</Message>
     <Message>This is awesome!</Message>
  </Response>"""

@app.route('/weather', methods=['GET', 'POST'])
def weather():
  return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>weather app</Message>

  </Response>"""


app.run(debug=True, host='0.0.0.0', port=8080)
