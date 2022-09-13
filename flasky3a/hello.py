from flask import Flask, render_template, session, redirect, url_for
from flask_moment import Moment
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Braxton'
moment = Moment(app)


@app.route('/weather/<name>')
def weather(name):
    alma_forecast_url = 'https://api.weather.gov/gridpoints/GRR/72,68/forecast'
    user_agent = 'Alma College CSC 121 Weather App; contact dextersd@alma.edu'
    headers = {'User-Agent': user_agent}
    weather_data = requests.get(alma_forecast_url, headers=headers).json()
    today = weather_data['properties']['periods'][0]
    session['temp'] = today['temperature']
    session['forecast'] = today['shortForecast']

    return render_template('weather.html',
                           name=name,
                           temp=today['temperature'],
                           forecast=today['shortForecast'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    session['user'] = name
    return render_template('user.html', name=name, url_time=f'/time/{name}',
                           url_temp=f'/weather/{name}')


@app.route('/time/<name>')
def time(name):
    return render_template('time.html', name=name, current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run()
