from .models import Url
from django import forms


class UrlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['short_url'].widget.attrs = {
            'placeholder': 'Enter a custom short URL',
            'id': 'short'
        }
        self.fields['original_url'].widget.attrs = {
            'placeholder': 'Enter a long URL to make it short',
            'id': 'original'
        }

    class Meta:
        model = Url
        fields = ('original_url', 'short_url', )
