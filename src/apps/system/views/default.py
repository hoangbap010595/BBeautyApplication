# Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


##
# Handle 404 Errors
# @param request WSGIRequest list with all HTTP Request
def handler404(request, *args, **argv):

    # 1. Load models for this view
    #from idgsupply.models import My404Method

    # 2. Generate Content for this view
    template = loader.get_template('shared/404.html')
    context = {

    }
    # 3. Return Template for this view + Data
    return HttpResponse(content=template.render(context),  status=404)


##
# Handle 500 Errors
# @param request WSGIRequest list with all HTTP Request
def handler500(request, *args, **argv):

    # 1. Load models for this view
    #from idgsupply.models import My404Method

    # 2. Generate Content for this view
    template = loader.get_template('shared/500.html')
    context = {

    }

    # 3. Return Template for this view + Data
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)
