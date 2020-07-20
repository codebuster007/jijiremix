from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagerTest(TestCase):
    """
    Test class for the custom user  manager
    """

    def setUp(self):
        self.ORMUser = get_user_model()

    def test_create_user(self):
        extra_fields = {
            'first_name': 'normal',
            'last_name': 'jijiremixuser',
            'residence_state': 'lagos',
        }
        user = self.ORMUser.objects.create_user(email='normal@hotmail.com',
                                                password='testuser', **extra_fields)
        
        self.assertEqual(user.email, 'normal@hotmail.com')

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            self.ORMUser.objects.create_user()
        with self.assertRaises(ValueError):
            self.ORMUser.objects.create_user(email='', password='')
        with self.assertRaises(ValueError):
            self.ORMUser.objects.create_user(email='', password='foo')


    def test_create_superuser(self):
        extra_fields = {
            'first_name': 'admin',
            'last_name': 'jijiremixadmin',
            'residence_state': 'world',
        }


        admin_user = self.ORMUser.objects.create_superuser(email='admin@jijiremix.com',
                                                           password='adminuser', **extra_fields)
        
        self.assertEqual(admin_user.email, 'admin@jijiremix.com')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(TypeError):
            self.ORMUser.objects.create_superuser()
        with self.assertRaises(ValueError):
            self.ORMUser.objects.create_superuser(email='', password='')
        with self.assertRaises(ValueError):
            self.ORMUser.objects.create_superuser(email='', password='foo')

        with self.assertRaises(ValueError):
            self.ORMUser.objects.create_superuser(
                email='admin@jijiremix.com', password='foo', is_superuser=False)
