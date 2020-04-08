from django.urls import path
from .views import PublisherList


app_name = 'bookstore'
urlpatterns = [
    path('publisher/', PublisherList.as_view(), name='publisher'),
]
