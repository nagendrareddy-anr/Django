from django.urls import path
from . import views


app_name='listing'

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing_ids'),
    path('search', views.search, name='search'),
]
