from __future__ import unicode_literals

from django.db import models


def image_upload_path(instance, filename):
    return filename


class Product(models.Model):
    active = models.CharField(max_length=200)
    cod = models.BooleanField()
    description = models.CharField(max_length=225)
    featured = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to=image_upload_path)
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    title = models.CharField(max_length=225)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    product = models.ManyToManyField(Product)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
