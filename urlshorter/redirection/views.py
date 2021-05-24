from django.shortcuts import get_object_or_404, redirect
from api.models import Link


def root(request, short_url):
    url = get_object_or_404(Link, short_url='http://' + short_url)

    return redirect(url.long_url)
