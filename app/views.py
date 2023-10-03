from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app.models import Categories
from django.core import serializers

# Create your views here.

def CATEGORIES(request):
    qs = list(Categories.objects.all())
    final_details = []
    for each in qs:
        details = {}
        category_info = vars(each)
        details['id'] = category_info['id']
        details['category_id'] = category_info['category_id']
        details['name'] = category_info['name']
        details['image'] = category_info['image']
        final_details.append(details)
    return JsonResponse({'status':200, 'category_details': final_details})
