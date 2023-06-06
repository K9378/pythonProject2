from datetime import datetime

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .filters import PostSearch
from .forms import PostForm
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'News.html'
    context_object_name = 'post'
    queryset = Post.objects.filter(category="NW")
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostSearch(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['new_news'] = None
        context['filterset'] = self.filterset
        return context

class NewsSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'search.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostSearch(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['new_news'] = None
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'sing_nw.html'
    context_object_name = 'post'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('news_list')


class ArticlesList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'Articles.html'
    context_object_name = 'post'
    queryset = Post.objects.filter(category="PO")

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostSearch(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['new_ar'] = None
        context['filterset'] = self.filterset
        return context


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'sing_ar.html'
    context_object_name = 'post'


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('news_list')

