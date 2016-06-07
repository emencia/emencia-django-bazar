import pytest
import factory

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from bazar.models import Entity, Note
from bazar.forms.entity import EntityForm
from bazar.forms.note import NoteForm

import factories


@pytest.mark.django_db
def test_form_entity(admin_client):
    """Simple test on Entity form"""
    entity_datas = factory.build(dict, FACTORY_CLASS=factories.EntityFormFactory)

    form = EntityForm(data=entity_datas)

    assert form.is_valid() == True

    form.save()

    assert Entity.objects.count() == 1


@pytest.mark.django_db
def test_form_note(admin_client):
    """Simple test on Note form"""
    factory_entity = factories.EntityModelFactory()

    note_datas = factory.build(dict, FACTORY_CLASS=factories.NoteFormFactory)

    # Save related object since we used build()
    author = note_datas.pop('author')
    entity = note_datas.pop('entity')
    author.save()
    entity.save()

    form = NoteForm(author=author, entity=entity, data=note_datas)

    # Submitted field values are valid
    assert form.is_valid() == True

    # Save note object
    note_instance = form.save()

    # Ensure foreignkey has been saved
    assert note_instance.author == author
    assert note_instance.entity == entity
