from django.urls import path
from .views import PublisherList, PublisherDetail


app_name = 'bookstore'
urlpatterns = [
    path('publisher/', PublisherList.as_view(), name='publisher'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher_detail'),
]
