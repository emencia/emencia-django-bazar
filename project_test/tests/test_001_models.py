import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from bazar.models import Entity, Note

from factories import UserFactory, EntityModelFactory, NoteModelFactory


def test_ping_index(admin_client):
    """Just pinging bazar index page"""
    response = admin_client.get(reverse('bazar:index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_factory_entity(admin_client):
    """Create an Entity object from factory"""
    factory_entity = EntityModelFactory()

    assert Entity.objects.count() == 1

    entity = Entity.objects.get(name=factory_entity.name)
    assert entity.phone == factory_entity.phone


@pytest.mark.django_db
def test_factory_note(admin_client):
    """Create Note objects from factory"""
    note_entity = NoteModelFactory()

    note = Note.objects.all()[0]

    # One user for admin_client, another one automatically from note subfactory
    assert User.objects.count() == 2
    # One entity from note subfactory
    assert Entity.objects.count() == 1
    # The created note
    assert Note.objects.count() == 1
    # At least one tag from previous note
    assert (note.tags.count()>0) == True
