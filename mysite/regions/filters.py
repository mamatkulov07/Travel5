from django_filters.rest_framework import FilterSet
from .models import HomePage, Review, Favorite


class HomePageFilter(FilterSet):
    class Meta:
        model = HomePage
        fields = {
            # 'name': ['exact'],
            'earth': ['gt', 'lt'],
        }


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'text': ['exact']
        }


class FavoriteFilter(FilterSet):
    class Meta:
        model = Favorite
        fields = {
            'region': ['exact']
        }

