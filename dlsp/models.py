from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    info = HTMLField()

    def __str__(self):
        return self.title


class SiteInfo(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    value = HTMLField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    acronym = models.CharField(max_length=10)
    info = models.TextField()

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    acronym = models.CharField(max_length=10)
    info = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')

