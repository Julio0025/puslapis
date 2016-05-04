from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from comments.forms import CommentForm
from .forms import postform
from .models import post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
def diskusijos(request):
    queryset_list = post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
        
    context = {
        "object_list":queryset,
        "title": "list"}
    return render(request, "diskusijos.html", context)




def diskusijos_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    form = postform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Sekmingai sukurta ")
        return HttpResponseRedirect(instance.get_absolute_url())

    
    context = { "form":form
        }
    return render(request, "diskusijos_create.html",context)

def diskusijos_detail(request, id):
    #instance = post.objects.get(id=0)
    instance = get_object_or_404(post, id=id)
    comment_form = CommentForm()
    comments = Comment.objects.filter_by_instance(instance)
    initial_data = {
    "content_type":instance.get_content_type,
    "object_id":instance.id
        }
    form = CommentForm(request.POST or None,initial= initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        content_type = ContentType.objects.get(model=c_type)
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
                
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj
            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    context = {
            
            "title":instance.title,
            "instance":instance,
            "id":instance.id,
            "comments":comments,
            "comment_form":form
    }
    return render(request, "diskusijos_detail.html", context)
    
    
def diskusijos_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=id)
    form = postform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sekmingai pakeista ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "title":instance.title,
            "instance":instance,
            "form":form
            }
    
    return render(request, "diskusijos_create.html",context)

def diskusijos_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=id)
    instance.delete()
    context = {"id":instance.id
       }
    return redirect("/diskusijos/")
    #return render(request, "diskusijos.html", context)


    








# Create your views here.
