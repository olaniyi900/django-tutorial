from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    

class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
    success_url = '/bookstore/publisher/'


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
    success_url = '/bookstore/publisher/'

class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher')