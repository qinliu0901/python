from django.db import models

# Create your models here.

# class Author(models.Model):
#     name=models.CharField(max_length=100)
#     age=models.ImageField(default=18)
#
# class Article(models.Model):
#     title=models.CharField(max_length=200)
#     content=models.TextField()
#     url=models.URLField()
#     portal=models.ImageField()
#     author=models.ForeignKey(Author)



class Author(models.Model):
    name=models.CharField(max_length=200)
    age=models.ImageField(default=18)

class Article(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    url=models.URLField()
    portal=models.ImageField()
    author=models.ForeignKey(Author)
