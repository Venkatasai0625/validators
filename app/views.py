from django.shortcuts import render
from app.forms import * 
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse(str(TFDO.cleaned_data))
        else:
            return HttpResponse("Invalid data")
    return render(request,'insert_topic.html',d)                
    
def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            #WO=Webpage.objects.get_or_create(topic_name=TO,NameError=na,url=url,email=email)
            #WO.save()
            return HttpResponse(str(WFDO.cleaned_data))
        else:
            return HttpResponse("Invalid data")
    
    
    return render(request,'insert_webpage.html',d)