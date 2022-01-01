from django import conf
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views import generic
from item.models import Item
from item.forms import FilterForm
from rest_framework import generics
from item.serializers import (
    ItemListSerializer,
    ItemCreateSerializers,
    ItemUpdateSerializer,
)
from django.db.models import QuerySet
from item import filters
from rest_framework.permissions import exceptions


class NewsListView(generic.ListView):
    model = Item
    paginate_by = 10
    template_name = "item/home.html"
    extra_context = {"form": FilterForm()}

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()

        news_items = [
            "job",
            "story",
            "poll",
        ]
        type_query = self.request.GET.get("type", None)
        text_query = self.request.GET.get("search", None)

        if type_query:
            if type_query in news_items:
                news_items = [type_query]

        queryset = queryset.filter(type__in=news_items)

        if text_query:
            queryset = queryset.filter(
                Q(title__icontains=text_query) | Q(text__icontains=text_query)
            )

        return queryset


class NewsItemListView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    filter_backends = [filters.NewsItemTextFilter, filters.NewsItemTypeFiler]
    search_fields = ["title", "type", "text"]
    queryset = Item.objects.all()


class NewsItemCreateView(generics.CreateAPIView):
    serializer_class = ItemCreateSerializers


class NewsItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Upate or delete an Item, returns an error if the Item is from the Hacker News api."""
    serializer_class = ItemUpdateSerializer
    queryset = Item.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ItemListSerializer
        return super().get_serializer_class()

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if (obj.local == False) and (request.method != "GET"):
            self.permission_denied(
                request, message="Cannot modify/delete a Hacker News Item.", code="619"
            )

    def permission_denied(self, request, message=None, code=None):
        if code == "619":
            raise exceptions.PermissionDenied(detail=message, code=code)
        return super().permission_denied(request, message=message, code=code)
