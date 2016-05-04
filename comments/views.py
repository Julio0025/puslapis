from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
def comment_delete(request, id)
    obj = get_object_or_404(comment, id = id)
    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "Istrinta")
    context = {
        "object":obj
        }
    return render(request, "confirm_delete.html", context)
# Create your views here.
