from django.shortcuts import render
from diskusijos.models import post
from django.http import HttpResponse
import feedparser
def index(request):
    queryset = post.objects.all().order_by("-timestamp")[0:3]
    feeds = feedparser.parse("http://feeds.feedburner.com/GamesLT")
    context = {
        "object_list":queryset,
        "title": "list",
        "feeds":feeds}
    return render(request, "home.html", context)

def duk(request):
    return render(request, 'duk.html')


