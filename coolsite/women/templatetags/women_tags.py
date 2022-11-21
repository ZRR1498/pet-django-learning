from django import template
from women.models import *


register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sotr=None, cat_selected=0):
    if not sotr:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sotr)

    return {"cats": cats, "cat_selected": cat_selected}
