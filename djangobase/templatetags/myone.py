from django import template

register = template.Library() #这里实例化对象名字 必须是register

@register.inclusion_tag('ul_list.html')
def num_list(num):
    num = 1 if num<1 else int(num)
    data = ['第{:0>3}号技师'.format(i) for i in range(1,num+1)]
    return {'mylist':data}
