from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

def all_user(request):
    return render(request, 'users/all_user.html')
