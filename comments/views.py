from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from diskusijos.models import post
from .models import Comment

def comment_delete(request, id):
    obj = get_object_or_404(Comment, id = id)
    parent_obj_url = obj.content_object.get_absolute_url()
    obj.delete()
    messages.success(request, "Komentaras istrintas")
    return HttpResponseRedirect(parent_obj_url)
    messages.success(request, "Istrinta")

    return redirect("/")
# Create your views here.
