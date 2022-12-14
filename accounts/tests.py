import email
from django.test import TestCase
from django.contrib.auth import get_user_model

# from accounts import admin

# # Create your tests here.
class CustomUserManagerTests(TestCase):
    
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(email='normal@mail.com',password='foo')
        self.assertEqual(user.email,'normal@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')  
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',password='foo')      

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(email='admin@mail.com',password='foo')

        self.assertEqual(admin_user.email,'admin@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)





class CustomUserModelTests(TestCase):


    def test__str__(self):
        User=get_user_model()
        user=User.objects.create_user(email='normal@mail.com',password='foo')
        self.assertEqual(str(user),user.email)
  
