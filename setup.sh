#!/bin/bash

# Setup Python Environment

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Django setup

cd src/

python manage.py migrate

python load.py &

# Setup and start redis server

wget http://download.redis.io/redis-stable.tar.gz

tar xvzf redis-stable.tar.gz

cd redis-stable

make

cd src/

./redis-server &

cd ../..

# Start celery worker

celery -A newsly worker -l INFO &

# Start celery beat

celery -A newsly beat &

# Run django server

python manage.py runserver
