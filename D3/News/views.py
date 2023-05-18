from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'News.html'
    context_object_name = 'post'
    queryset = Post.objects.filter(category="NW")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['new_news'] = None
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'id.html'
    context_object_name = 'post'
