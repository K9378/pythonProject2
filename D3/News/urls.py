from django.urls import path
from .views import NewsList, NewsDetail, ArticlesList, ArticlesDetail, NewsCreate, NewsDelete, ArticlesDelete, \
   NewsSearch, NewsUpdate


class NewsEdit:
   pass


urlpatterns = [
   path('news/', NewsList.as_view(), name='news_list',),
   path('news/<int:pk>', NewsDetail.as_view(), name='news_detail',),
   path('news/create/', NewsCreate.as_view(), name='news_create',),
   path('search/', NewsSearch.as_view(), name='news_search',),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit',),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete',),
   path('articles/', ArticlesList.as_view(), name='ar_list',),
   path('articles/<int:pk>', ArticlesDetail.as_view(), name='ar_detail',),
   path('articles/create/', NewsCreate.as_view(), name='news_create',),
   path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit',),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='ar_delete',),
]