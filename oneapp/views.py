from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .models import Url
from .forms import UrlForm


class ShortenView(CreateView):
    template_name = 'home.html'
    form_class = UrlForm


def validate_url(request):
    url = request.GET.get('url', None)
    data = {
        'is_taken': Url.objects.filter(short_url__iexact=url).exists(),
        'invalid_length': len(url) > 30
    }
    return JsonResponse(data)
