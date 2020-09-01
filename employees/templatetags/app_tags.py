from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def url_add_query(context, **kwargs):
    request = context.get('request')
    query = request.GET.copy()
    try:
        query.pop('page')
    except KeyError:
        pass
    query.update(kwargs)
    return query.urlencode()