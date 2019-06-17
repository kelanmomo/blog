from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    # response = list()
    # for category in categories:
    #     response.append(category)
    #     response.append('<br>')
    return render(request, 'home.html', {'categories':categories})
