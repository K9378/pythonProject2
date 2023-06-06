from django.forms import DateTimeInput
from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateTimeFilter
from .models import Post, Category


class PostSearch(FilterSet):



   post_cat = ModelChoiceFilter(
       field_name='post_cat',
       queryset=Category.objects.all(),
       label='Категория',
       empty_label='Любая'
   )

   title = CharFilter(
       field_name='title',
       lookup_expr='icontains',
       label='Заголовок',
   )

   text = CharFilter(
       field_name='text',
       lookup_expr='icontains',
       label='Текст',
   )

   date = DateTimeFilter(
       field_name='time_in',
       lookup_expr='gt',
       label='Дата создания',
       widget=DateTimeInput(
           format='%Y-%m-%dT%H:%M',
           attrs={'type': 'datetime-local'},
       )

   )

   class Meta:
       model = Post
       fields = {
           'category': ['exact'],
       }

