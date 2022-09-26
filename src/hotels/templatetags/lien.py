from django import template

register = template.Library()


@register.filter
def lien(l):
    li = l+'Ben'
    return li
