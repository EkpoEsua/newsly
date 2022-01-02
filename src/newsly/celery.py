import os
from load import load_items

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsly.settings")

app = Celery("newsly")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task(name="newsly.celery.load_data_from_api")
def load_data_from_api():
    """Celery task to initiate the "load_items" function, which loads news items into the database."""
    print("Started loading api data into the database.")
    load_items()
    print("Done loading new items.")

