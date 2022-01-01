from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title="Newsly API.",
    # url="127.0.0.0:8000/",
    description="Returns fetched Hacker news and Newsly news.",
    version="v1.0.0"
)
