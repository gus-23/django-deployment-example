from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    corta fora todos valores de "arg" da string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
