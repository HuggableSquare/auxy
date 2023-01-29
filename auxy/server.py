import streamlink
import requests
from flask import redirect
from auxy import app

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/twitch/<user>')
def twitch_user(user):
    return redirect(streamlink.streams(f'https://www.twitch.tv/{user}')['audio_only'].url)

@app.route('/iheart/<station>')
def iheart_station(station):
    response = requests.get(f'https://us.api.iheart.com/api/v2/content/liveStations/{station}')
    return redirect(response.json()['hits'][0]['streams']['secure_shoutcast_stream'])
