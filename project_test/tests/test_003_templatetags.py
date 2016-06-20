import pytest
import factory

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from bazar.settings import ENTITY_KINDS, DEFAULT_ENTITY_KIND
from bazar.templatetags.bazar_tags import get_kind_display


def test_kind_display_001():
    """Default entity name"""
    assert get_kind_display(DEFAULT_ENTITY_KIND) == dict(ENTITY_KINDS)[DEFAULT_ENTITY_KIND]


def test_kind_display_002():
    """Entity 'internal' name"""
    assert get_kind_display('internal') == dict(ENTITY_KINDS)['internal']


def test_kind_display_003():
    """Error on unknowed entity from kinds"""
    with pytest.raises(AttributeError):
        # template tags are lazy, need to use a print to force execution
        print get_kind_display('foo')
