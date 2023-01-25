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
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    date=models.DateTimeField(auto_now_add = True)
    borrower_name=models.CharField(max_length =50)
    borrower_email=models.EmailField(max_length=50)
    book=models.ForeignKey(
        Book,
        related_name="book",
        on_delete=models.CASCADE)
