from django.test import TestCase

from ..models import ORMUser

class UserModelTest(TestCase):
    """
    Test module for the custom user model
    """

    
    def setUp(self):
        self.__create_dummy_data()

    def test_jwt_secret_is_created(self):
        john = ORMUser.objects.get(email='johndoe@gmail.com')
        sarah = ORMUser.objects.get(email='sarahdoe@hotmail.com')
        david = ORMUser.objects.get(email='davidoe@jijiremix.com')
        admin = ORMUser.objects.get(email='admin@jijiremix.com')

        self.assertIsNotNone(john.jwt_secret)
        self.assertIsNotNone(sarah.jwt_secret)
        self.assertIsNotNone(david.jwt_secret)
        self.assertIsNotNone(admin.jwt_secret)

    def test_residence_state_is_not_blank(self):
        john = ORMUser.objects.get(email='johndoe@gmail.com')
        sarah = ORMUser.objects.get(email='sarahdoe@hotmail.com')
        david = ORMUser.objects.get(email='davidoe@jijiremix.com')
        admin = ORMUser.objects.get(email='admin@jijiremix.com')

        self.assertNotEqual(john.jwt_secret, '')
        self.assertNotEqual(sarah.jwt_secret, '')
        self.assertNotEqual(david.jwt_secret, '')
        self.assertNotEqual(admin.jwt_secret, '')

    def __create_dummy_data(self):
        extra_fields = {
            'first_name': 'john',
            'last_name': 'doe',
            'residence_state': 'lagos',
        }
        ORMUser.objects.create_user(
            email='johndoe@gmail.com', password='foo',
            **extra_fields
        )
        extra_fields2 = {
            'first_name': 'sarah',
            'last_name': 'doe',
            'residence_state': 'abuja',
        }
        ORMUser.objects.create_user(
            email='sarahdoe@hotmail.com', password='foobar',
            **extra_fields2
        )
        extra_fields3 = {
            'first_name': 'david',
            'last_name': 'doe',
            'residence_state': 'lagos',
        }
        ORMUser.objects.create_superuser(
            email='davidoe@jijiremix.com', password='foobarfoo',
            **extra_fields3
        )
        extra_fields4 = {
            'first_name': 'admin',
            'last_name': 'user',
        }
        ORMUser.objects.create_superuser(
            email='admin@jijiremix.com', password='foobarfoobar',
            **extra_fields4
        )