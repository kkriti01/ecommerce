from django.contrib.sessions.models import Session
from django.db import models


from account.models import Myuser


class CartItem(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
