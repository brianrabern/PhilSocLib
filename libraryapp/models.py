from django.db import models


class Book(models.Model):
    call_number = models.CharField(max_length =50)
    author = models.CharField(max_length =100)
    title = models.CharField(max_length =100)
    year = models.CharField(max_length =50)
    publisher = models.CharField(max_length =100)
    isbn = models.CharField(max_length =100)
    inventory = models.CharField(max_length =50)
    language = models.CharField(max_length =100)
    notes = models.TextField(null=True)
