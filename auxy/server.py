import streamlink
from flask import Flask, redirect
from auxy import app

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/twitch/<user>')
def twitch_user(user):
    return redirect(streamlink.streams(f'https://www.twitch.tv/{user}')['audio_only'].url)
