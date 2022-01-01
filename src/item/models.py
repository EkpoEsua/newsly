from django.db import models
import datetime


def default_array():
    """Return an empty array as default value for the array fields of the Item model."""
    return []


TYPE_CHOICES = [
    ("job", "job"),
    ("story", "story"),
    ("comment", "comment"),
    ("poll", "poll"),
    ("pollopt", "pollopt"),
]


class Item(models.Model):
    hacker_news_id = models.BigIntegerField(default=-1, blank=True)
    newsly_news_id = models.BigIntegerField(default=-1, blank=True)
    local = models.BooleanField(default=False, blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES
    )  # use a validator for this field
    by = models.CharField(max_length=300, default="", blank=True)
    time = models.BigIntegerField(default=-1, blank=True)
    dead = models.BooleanField(default=False, blank=True)
    kids = models.JSONField(default=default_array, blank=True)
    parts = models.JSONField(default=default_array, blank=True)
    text = models.TextField(default="", blank=True)
    url = models.URLField(default="", blank=True)
    title = models.TextField(default="", blank=True)
    descendants = models.IntegerField(default=-1, blank=True)
    score = models.IntegerField(default=-1, blank=True)
    parent = models.BigIntegerField(default=-1, blank=True)

    class Meta:
        ordering = ["-time"]
        indexes = [
            models.Index(
                fields=[
                    "id",
                    "type",
                    "-time",
                    "title",
                    "text",
                    "hacker_news_id",
                    "newsly_news_id",
                    "local",
                ],
                name="table_indexes",
            )
        ]

    def posix_time_to_datetime_object(self):
        return datetime.datetime.fromtimestamp(self.time)


# class NewslyItem(models.Model):
#     deleted = models.BooleanField(default=False, blank=True)
#     type = models.CharField(max_length=50, choices=TYPE_CHOICES)
#     by = models.CharField(max_length=300, default="", blank=True)
#     time = models.BigIntegerField(default=-1, blank=True)
#     dead = models.BooleanField(default=False, blank=True)
#     kids = models.JSONField(default=default_array, blank=True)
#     parts = models.JSONField(default=default_array, blank=True)
#     text = models.TextField(default="", blank=True)
#     url = models.URLField(default="", blank=True)
#     title = models.TextField(default="", blank=True)
#     descendants = models.IntegerField(default=-1, blank=True)
#     score = models.IntegerField(default=-1, blank=True)
#     parent = models.BigIntegerField(default=-1, blank=True)

#     class Meta:
#         ordering = ["-time"]
#         indexes = [
#             models.Index(
#                 fields=["id", "type", "-time", "title", "text"],
#                 name="newsly_table_indexes",
#             )
#         ]

#     def posix_time_to_datetime_object(self):
#         return datetime.datetime.fromtimestamp(self.time)
