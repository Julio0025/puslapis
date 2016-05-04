from django.shortcuts import render
from diskusijos.models import post
from django.http import HttpResponse


def index(request):
    queryset = post.objects.all().order_by("-timestamp")[0:3]
    context = {
        "object_list":queryset,
        "title": "list"}
    return render(request, "home.html", context)

def duk(request):
    return render(request, 'duk.html')

