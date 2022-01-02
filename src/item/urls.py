from django.urls import path
from django.views.generic.base import TemplateView
from item import views
from item import schema

urlpatterns = [
    path("", views.NewsListView.as_view(), name="list-news"),
    path("item/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"),
    path("api/item/", views.NewsItemListView.as_view(), name="list-items"),
    path("api/item/create/", views.NewsItemCreateView.as_view(), name="create-item"),
    path(
        "api/item/<int:pk>/",
        views.NewsItemUpdateDeleteView.as_view(),
        name="delete-updare-item",
    ),
    path("api/openapi/", schema.schema_view, name="openapi-schema"),
    path(
        "api/doc/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
