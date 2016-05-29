import random

import factory

from django.conf import settings
from django.contrib.auth.models import User

from bazar.models import Entity, Note

# Some sample tag to pick
NOTE_TAGS_SAMPLES = [
    "cat",
    "dog",
    "apple",
    "peach",
    "lorem ipsum",
]


class UserFactory(factory.django.DjangoModelFactory):
    """
    Simple factory for User model
    """
    first_name = factory.Sequence(lambda n: 'Firstname {0}'.format(n))
    last_name = factory.Sequence(lambda n: 'Lastname {0}'.format(n))
    username = factory.LazyAttribute(lambda obj: '{0}.{1}'.format(obj.first_name.lower().replace(' ', '_'), obj.last_name.lower().replace(' ', '_')))
    email = factory.LazyAttribute(lambda obj: '{0}.{1}@example.com'.format(obj.first_name.lower().replace(' ', '_'), obj.last_name.lower().replace(' ', '_')))

    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    is_superuser = False
    is_staff = False
    is_active = True

    class Meta:
        model = User


class EntityFactory(factory.django.DjangoModelFactory):
    """
    Factory for Entity model with default kind
    """
    kind = settings.DEFAULT_ENTITY_KIND

    name = factory.Faker('name', locale='fr_FR')
    adress = factory.Faker('street_address', locale='fr_FR')
    phone = factory.Faker('phone_number', locale='fr_FR')
    fax = factory.Faker('phone_number', locale='fr_FR')
    town = factory.Faker('city', locale='fr_FR')
    zipcode = factory.Faker('postcode', locale='fr_FR')

    class Meta:
        model = Entity


class NoteFactory(factory.django.DjangoModelFactory):
    """
    Factory for Note model

    file = models.FileField(_('file'), upload_to=get_file_uploadto, storage=ATTACHMENT_FS_STORAGE, max_length=255, null=True, blank=True)
    """
    author = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)

    title = factory.Faker('sentence', locale='fr_FR', nb_words=6, variable_nb_words=True)
    content = factory.Faker('text', locale='fr_FR', max_nb_chars=500)

    file = factory.Faker('file_name', category=None, extension=None)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        After object is created we can add some tags
        """
        obj = model_class(*args, **kwargs)
        obj.save()

        # Choose a random set of random tags to add
        tags_count = random.randint(1, len(NOTE_TAGS_SAMPLES))
        tags = random.sample(NOTE_TAGS_SAMPLES, tags_count)
        obj.tags.add(*tags)

        return obj

    class Meta:
        model = Note
