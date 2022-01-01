from datetime import datetime
from typing import OrderedDict
from rest_framework import serializers
from item.models import Item


class ItemCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "type",
            "by",
            "kids",
            "parts",
            "text",
            "url",
            "title",
            "descendants",
            "score",
            "parent",
        ]
        extra_kwargs = {
            "kids":{
                "default": [],
                "initial": [],
            },
            "parts":{
                "default":[],
                "initial": [],
            }
        }
    
    def save(self, **kwargs):
        if self.instance:
            time = self.instance.time
        else:
            time = datetime.timestamp(datetime.now())

        instance: Item = super().save(time=time, local=True, **kwargs)
        instance.newsly_news_id = instance.pk
        instance.save()
        return instance


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "deleted",
            "type",
            "by",
            "dead",
            "kids",
            "parts",
            "text",
            "url",
            "title",
            "descendants",
            "score",
            "parent",
        ]


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "hacker_news_id",
            "newsly_news_id",
            "deleted",
            "type",
            "by",
            "time",
            "dead",
            "kids",
            "parts",
            "text",
            "url",
            "title",
            "descendants",
            "score",
            "parent",
        ]

    def to_representation(self, instance):
        """Return the output of the serializer without fields having default values."""
        ret: OrderedDict = super().to_representation(instance)

        keys = list(ret.keys())
        for key in keys:
            field_value = self.Meta.model._meta.get_field(key).default
            if callable(field_value):
                if field_value() == ret[key]:
                    ret.pop(key)
            else:
                if field_value == ret[key]:
                    ret.pop(key)
        return ret
    
