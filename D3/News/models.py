from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    au_user = models.OneToOneField(User, on_delete=models.CASCADE)
    au_rating = models.IntegerField(default=0)

    def __str__(self):
        return f' {self.au_user}'

    def update_rating(self):
        pr = self.post_set.aggregate(post_rating=Sum('post_rating'))
        prate = 0
        prate += pr.get('post_rating')

        cr = self.au_user.comment_set.aggregate(com_rating=Sum('com_rating'))
        crate = 0
        crate += cr.get('com_rating')

        self.au_rating = prate * 3 + crate
        self.save()


class Category(models.Model):
    cat_type = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f' {self.cat_type}'


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    POST = 'PO'
    CATEGORY_POST = ((NEWS, 'Новость'), (POST, 'Статья'))
    category = models.CharField(max_length=2, choices=CATEGORY_POST, default=POST)
    time_in = models.DateTimeField(auto_now_add=True)
    post_cat = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ...'

    def __str__(self):
        return f' {self.category} {self.id} {self.post_author}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    pc_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pc_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.pc_category}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
