from django import template
 
 
register = template.Library()
 
@register.filter(name="multiply")
def multipliy(height, weight):
    return weight /  ((height / 100) * (height / 100))
