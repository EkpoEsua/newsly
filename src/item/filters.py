from rest_framework import filters
from django.utils.translation import gettext_lazy as _


class NewsItemTextFilter(filters.SearchFilter):
    search_param = "search"
    search_title = _("Text Search.")
    search_description = _(
        "Text based search on the text and title field of news items."
    )

    def get_search_fields(self, view, request):
        return ["title", "text"]


class NewsItemTypeFiler(filters.SearchFilter):
    search_param = "type"
    search_title = _("Type search.")
    search_description = _(
        """Filter the News Item by type, "job", "story", "comment", "poll", or "pollopt"."""
    )

    def get_search_fields(self, view, request):
        return ["type"]
