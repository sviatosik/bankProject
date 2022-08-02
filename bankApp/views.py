from django.shortcuts import render,get_object_or_404
from .models import Client, Bank
from django.db.models import Q

# Create your views here.


def show_info(request):
    peoples = Client.objects.all()
    context = {'people': peoples}
    return render(request, 'bankApp/one.html', context=context)


