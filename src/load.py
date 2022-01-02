import django
import os
import requests
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsly.settings")
django.setup()

from item.models import Item
from django.db.models import Max


def hit_end_point(url: str) -> str:
    """Return the text response from a request to a url"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(e)
        return None


def save_item(item_data: dict) -> bool:
    """Saves an news item to the database given it's attribute values as dict."""
    if item_data:
        hacker_news_id = item_data.pop("id")
        item_data["hacker_news_id"] = hacker_news_id
        try:
            item = Item(**item_data)
        except Exception as e:
            print(e)
            return False
        item.save()
        return True
    return False


def get_item(item_id: int) -> dict:
    """Return a news item as a dict from the hackernews api given it's id"""
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    response = hit_end_point(url)
    if response:
        item_data = json.loads(response)
        return item_data
    return None


def load_items():
    """Load multiple item to the database.
    On first time initialization, the last 100 items are loaded to the database.
    Else the new items since last poll to recent item is loaded.
    """
    q = Item.objects.aggregate(Max("hacker_news_id"))
    max_id = q["hacker_news_id__max"]
    url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
    try:
        max_item_id = int(hit_end_point(url))
    except Exception as e:
        print(e)
        return False
    if max_id:
        star_id = max_id + 1
    else:
        star_id = max_item_id - 100

    for item_id in range(star_id, max_item_id + 1):
        out_come = save_item(get_item(item_id))
        print(f"Progress: {item_id} / {max_item_id-star_id} ")
    return True


if __name__ == "__main__":
    out_come = load_items()
    if out_come:
        print("Loaded new items.")
    else:
        print("Error Loading new items.")
