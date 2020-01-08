from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

def index(request):
    template = loader.get_template('AIA/index.html')
    context = {
    
    }
    return HttpResponse(template.render( context ,request))
    # return HttpResponse('hello world')
