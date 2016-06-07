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


class EntityFactory(factory.Factory):
    """
    Base factory for Entity with default kind
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


class EntityFormFactory(EntityFactory):
    """
    Factory for Entity datas to give to Entity forms
    """
    class Meta:
        abstract = False
        strategy = factory.BUILD_STRATEGY


class EntityModelFactory(EntityFactory, factory.django.DjangoModelFactory):
    """
    Factory for Entity model
    """
    class Meta:
        abstract = False


class NoteFactory(factory.django.DjangoModelFactory):
    """
    Base factory for Note model
    """
    author = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityModelFactory)

    title = factory.Faker('sentence', locale='fr_FR', nb_words=6, variable_nb_words=True)
    content = factory.Faker('text', locale='fr_FR', max_nb_chars=500)

    file = factory.Faker('file_name', category=None, extension=None)

    @classmethod
    def make_some_random_tags(self):
        """Choose a random set of random tags to add"""
        tags_count = random.randint(1, len(NOTE_TAGS_SAMPLES))
        tags = random.sample(NOTE_TAGS_SAMPLES, tags_count)

        return tags

    class Meta:
        model = Note


class NoteFormFactory(NoteFactory):
    """
    Factory for Note datas to give to Entity forms
    """
    @factory.lazy_attribute
    def tags(self):
        """
        Return a Python list, because its the attempted type with form field
        """
        return NoteFormFactory.make_some_random_tags()

    class Meta:
        abstract = False
        strategy = factory.BUILD_STRATEGY


class NoteModelFactory(NoteFactory, factory.django.DjangoModelFactory):
    """
    Factory for Note model
    """
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        After object is created we can add some tags
        """
        obj = model_class(*args, **kwargs)
        obj.save()

        # Choose a random set of random tags to add
        obj.tags.add(*cls.make_some_random_tags())

        return obj

    class Meta:
        abstract = False
