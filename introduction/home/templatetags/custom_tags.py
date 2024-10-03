from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import bleach

register = template.Library()


@register.filter(name='allow_safe_tags')
@template.defaultfilters.stringfilter
def allow_safe_tags(value):
    """
    Erlaubt nur bestimmte HTML-Tags (z.B. <b>, <br>, <i>, <u>) und rendert den Text sicher.
    """
    if value:
        # Liste der erlaubten Tags erweitern
        allowed_tags = ['b']
        cleaned_value = bleach.clean(value, tags=allowed_tags, strip=True)
        # Markiert den bereinigten Text als sicher
        return mark_safe(cleaned_value)
    return value

@register.filter(name='range')
def range_filter(value):
    print(value)
    """Returns a range object up to the given value."""
    return range(int(value))