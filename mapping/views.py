from django.shortcuts import render
from mapping.models import Tweets
from django.template import RequestContext, loader
# Create your views here.
def index(request, keyword):
    latings = []
    if keyword!="":
        for tweets in Tweets.objects.filter(keywords=keyword):
            latings.append([tweets.latitude,tweets.longitude])
    else:
        for tweets in Tweets.objects.all():
            latings.append([tweets.latitude,tweets.longitude])
    print latings
    context = {'latlngs': latings}
    return render(request, 'mapping/maptest.html', context)


