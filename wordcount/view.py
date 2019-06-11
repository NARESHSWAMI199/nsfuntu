from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'index.html',{'name':'By Naresh swami'})

def counts(request):
    data = request.GET["text_area"]
    data_list= data.split()
    data_length = len(data_list)
    dictonry = {}
    for i in data_list:
        dictonry[i] = data_list.count(i)
    d = sorted(dictonry.items(), key = operator.itemgetter(1),reverse =True)

    return render(request,'count.html',{'text_area':data,"words":data_length, 'repeat':d})

def about_me(request):
    return render(request,'aboutme.html')

    
        


    
    
   
