from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from bookstore.models import Publisher, Book, Author


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context


class BookListView(ListView):
    queryset = Book.objects.order_by('-publication_date')
    