from django.db import models

class UserTable(models.Model):
    user_type_choices = (
        (1,'普通用户'),
        (2,'vip'),
        (3,'svip'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32,unique=True) #这里的unique是唯一索引，就是此用户名不能重复
    password = models.CharField(max_length=64)
    id_2 = models.CharField(max_length=10)

class UserToken(models.Model): # 这里是token的结构
    user = models.OneToOneField(to = 'UserTable')  #这里是把token与UserTable 形成一对一关系机构
    token = models.CharField(max_length=64) #定义token字段

# Create your models here.
