from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomUserTest(TestCase):
    def test_add_user(self):
        user = get_user_model().objects.create_user(
            username='user1',
            email='user1@mail.com',
            password='pass123!'
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser(self):
        user = get_user_model().objects.create_superuser(
            username='user1',
            email='user1@mail.com',
            password='pass123!'
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@mail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
