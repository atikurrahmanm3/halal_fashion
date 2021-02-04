from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    datetime.datetime.now()
    return render(request,'index.html')