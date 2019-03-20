from guestBook.models import GuestBookEntry
from django.forms import ModelForm


class GuestBookEntryForm(ModelForm):
    class Meta:
        model= GuestBookEntry
        fields = ['extra','cost','quantity']