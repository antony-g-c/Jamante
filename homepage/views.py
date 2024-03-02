from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import product

def Product_view(request):
    mymembers = product.objects.all().values()
    template = loader.get_template('products.html')
    context = {
        'mymembers': mymembers,
               }
    return HttpResponse(template.render(context,request))

def details(request, id):
  mymember = product.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context,request))
