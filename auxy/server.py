import streamlink
import requests
from configparser import ConfigParser
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
    station_response = requests.get(f'https://us.api.iheart.com/api/v2/content/liveStations/{station}')
    streams = station_response.json()['hits'][0]['streams']
    if 'secure_shoutcast_stream' in streams:
        return redirect(streams['secure_shoutcast_stream'])
    elif 'secure_pls_stream' in streams:
        pls_response = requests.get(streams['secure_pls_stream'])
        parser = ConfigParser()
        parser.read_string(pls_response.text)
        return redirect(parser['playlist']['File1'])
    return
