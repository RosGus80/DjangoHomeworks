from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    """convert relative path to absolute path"""
    if val:
        return f'/previews/{val}'
    else:
        return ''


