from django.forms import ModelForm
from django import forms
from libraryapp.models import Borrow


class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = [
            "borrower_name",
            "borrower_email",
            "book"
        ]
        widgets = {
            'book': forms.HiddenInput(),
        }
