from django.urls import path

from apis.ratings.bindings import star_rating_view


urlpatterns = [
    path('star-rating/<uuid:item__uuid>/', star_rating_view, name='star-rating'),
]
