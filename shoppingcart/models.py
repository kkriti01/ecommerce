import json
from time import time


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    status_choice = (
        ('initiated': 'initiated'),
        ('proce'))
