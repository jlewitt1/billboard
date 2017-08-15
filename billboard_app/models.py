# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import timezone

from django.db import models


# Create your models here.

class Post(models.Model):
    posts_text = models.CharField(max_length = 255)
    posts_title = models.CharField(max_length=100)
    posts_author = models.CharField(max_length=100)
    posts_pub_date = models.DateTimeField('date posted')

    def __str__(self):  # __unicode__ on Python 2
        return self.posts_title

