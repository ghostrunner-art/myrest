from django.http import JsonResponse
from rest_framework.views import APIView
from myrestapp import models


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()  # 用hexdigest()就是返回的md5的字符串


class AuthView(APIView):  # 这里的restframework框架的APIView是继承django.views里面的View
    # def get(self,request,*args,**kwargs):     #这里是CBV方式的get请求的固定格式
    #     self.dispatch()
    #     ret = {
    #         'id':100,
    #         'name':'hanmeimei',
    #         'age':12,
    #     }
    #     return JsonResponse()
    def post(self, request, *args, **kwargs):
        # 这里千万注意，这里的第一个request是restframework封装的，要取原生的request要用_request
        res = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserTable.objects.filter(username=user, password=pwd).first()
            if not obj:
                res['code'] = 1001
                res['msg'] = "用户名密码不正确"
            token = md5(user)  # 这里取到用户对应的md5的字符串
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            res['token'] = token
        except Exception as e:
             res['code'] = 131213
             res['msg'] = '未知错误'
        return JsonResponse(res)

    #
    # def put(self,request,*args,**kwargs):
    #     pass
    # def delete(self,request,*args,**kwargs):
    #     pass
