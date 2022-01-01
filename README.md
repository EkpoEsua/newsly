In the project folder, run the setup script.
```
./setup.sh
```
OR

# Setup Python Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Django setup
```
cd src/
python manage.py migrate
```

# Setup and start redis server
```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
cd src/
./redis-server &
cd ../..
```

# Start celery worker
```
celery -A newsly worker -l INFO &
```

# Start celery beat
```
celery -A newsly beat &
```

# Run django server
```
python manage.py runserver
```

# Docs/Guide for the api
[127.0.0.1:800/api/doc/](127.0.0.1:800/api/doc/)
