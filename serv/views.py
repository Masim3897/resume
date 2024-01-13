from django.shortcuts import render

import serv

# Create your views here.

def services(request):
    return render(request, 'serv/services.html')
