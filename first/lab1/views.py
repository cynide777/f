from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body><h1>the datetime now %s</h1></body></html>"%now
    return HttpResponse(html)

def fha(request):
    now=datetime.datetime.now()+datetime.timedelta(hours=4)
    html="<html><body><h1>the datetime now %s</h1></body></html>"%now
    return HttpResponse(html)
def fhb(request):
    now=datetime.datetime.now()+datetime.timedelta(hours=-4)
    html="<html><body><h1>the datetime now %s</h1></body></html>"%now
    return HttpResponse(html)
def fhao(request,offset):
    now=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body><h1>the datetime now %s</h1></body></html>"%now
    return HttpResponse(html)
def fhbo(request,offset):
    now=datetime.datetime.now()+datetime.timedelta(hours=-offset)
    html="<html><body><h1>the datetime now %s</h1></body></html>"%now
    return HttpResponse(html)
