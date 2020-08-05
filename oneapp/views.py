from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse
from .models import Url
from .forms import UrlForm


# class ShortenView(CreateView):
#     template_name = 'home.html'
#     form_class = UrlForm


def shorten_view(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            original = form.cleaned_data.get('original_url')
            short = form.cleaned_data.get('short_url')
            return redirect('success_page', data=short)
    else:
        form = UrlForm()
    return render(request, 'home.html', {'form': form})


def validate_url(request):
    url = request.GET.get('url', None)
    data = {
        'is_taken': Url.objects.filter(short_url__iexact=url).exists(),
    }
    return JsonResponse(data)


def success_view(request, data):
    return render(request, 'success.html', {'data': data})


def url_redirection_view(request, new_short_url):
    url = get_object_or_404(Url, short_url=new_short_url)
    redirection_url = url.original_url
    return HttpResponseRedirect(redirection_url)
    