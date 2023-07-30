
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# class based views

#  function based views

def homeview(request):
    return render(request, 'index.html')


def contact_view(request):
    return render(request, 'contacts.html')


def profile_view(request):
    return render(request, 'profile.html')