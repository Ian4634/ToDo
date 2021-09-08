from django import template

register = template.Library()


@register.simple_tag
def indexing_list(list1, index):
    return list1[index]


@register.simple_tag
def delete():
    return 'delete'

@register.simple_tag
def add1(num):
    return num+1