from django.urls import path
from .views import (PublisherList, PublisherDetail, 
                    BookListView, PublisherCreateView, 
                    PublisherUpdateView, PublisherDeleteView)


app_name = 'bookstore'
urlpatterns = [
    path('publisher/', PublisherList.as_view(), name='publisher'),
    path('publisher/add/', PublisherCreateView.as_view(), name='publisher-add'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher_detail'),
    path('publisher/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher_delete'),
    path('book/', BookListView.as_view(), name='book'),
    
]
