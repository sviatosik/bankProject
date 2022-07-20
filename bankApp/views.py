from django.shortcuts import render,get_object_or_404
from .models import Client
from django.db.models import Q

# Create your views here.


def show_info(request):
    peoples = Client.objects.filter(Q(client_age__gt =18) ,Q(cart_balance__gt = 10000))
    context = {'people': peoples}
    return render(request, 'bankApp/one.html', context=context)


