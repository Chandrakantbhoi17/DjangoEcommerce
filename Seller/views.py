from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def Filter(request,query):
   
    return HttpResponse(query)
