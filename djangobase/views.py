from django.shortcuts import render,HttpResponse
from djangobase import models


# Create your views here.
def baseone(request):
    # req = request.POST.get('daan1',None)
    # print(req)

    que=models.Que.objects.all()

    return render(request,'wenti_zheli.html',{'ques':que})