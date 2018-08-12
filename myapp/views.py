from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
import json

class Dingdan(APIView):#这里的restframework框架的APIView是继承django.views里面的View
    def get(self,request,*args,**kwargs):
        ret = {
            'id':100,
            'name':'hanmeimei',
            'age':12,
        }
        return HttpResponse(json.dumps(ret),status=200)
    def post(self,request,*args,**kwargs):
        pass
    def put(self,request,*args,**kwargs):
        pass
    def delete(self,request,*args,**kwargs):
        pass
