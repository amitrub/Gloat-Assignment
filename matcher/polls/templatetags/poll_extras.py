from django import template
from django.utils.encoding import iri_to_uri
from django.utils.html import escape
from rest_framework.utils.urls import remove_query_param, replace_query_param
from urllib import parse

from django.utils.encoding import force_str

register = template.Library()


@register.simple_tag
def add_query_param1(request, key, val):
    """
    Add a query parameter to the current request url, and return the new url.
    """
    iri = request.get_full_path()
    uri = iri_to_uri(iri)
    out = escape(replace_query_param(uri, key, val))
    return out
