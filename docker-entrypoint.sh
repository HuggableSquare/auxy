#!/usr/bin/env sh

poetry run gunicorn 'auxy:app' -b 0.0.0.0
