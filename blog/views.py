from django.shortcuts import render
from .models import blog
# Create your views here.
def blogs(request):
    blogdata = blog.objects.all()
    context = {
        'blog':blogdata,
    }
    return render(request,"blogs.html",context)