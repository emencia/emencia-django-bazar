"""
Some markup utilities for RST and DjangoCodeMirror usage

TODO: rst/djangocodemirror formatting should not be the default formatting,
      because they are not package requirements.
"""
from django.forms import ValidationError

from rstview.parser import SourceReporter, map_parsing_errors

from djangocodemirror.fields import DjangoCodeMirrorField

def get_text_field(form_instance, **kwargs):
    """
    Return a DjangoCodeMirrorField field
    """
    kwargs.update({
        'config_name': 'bazar'
    })
    return DjangoCodeMirrorField(**kwargs)


def clean_restructuredtext(form_instance, content):
    """
    RST syntax validation
    """
    if content:
        errors = SourceReporter(content)
        if errors:
            raise ValidationError(map(map_parsing_errors, errors))
    return content
