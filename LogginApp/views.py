from django.shortcuts import render
from .models import Persona
import logging
import datetime
from django.http import HttpResponse

# Create your views here.

logger=logging.getLogger(__name__)

def hello_reader(request):
    logger.warning('Se ha accedido a la página de inicio del'+str(datetime.datetime.now())+'horaas')
    return HttpResponse('Logging')

def home(request):
    personas=Persona.objects.all()
    context={'personas':personas}
    return render(request, 'index.html', context)