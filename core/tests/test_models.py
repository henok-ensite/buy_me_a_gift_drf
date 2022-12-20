"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Tests for models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is succesful."""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails=[
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@Example.com', 'TEST3@example.com'],
            ['test4@Example.com', 'test4@example.com'],
        ]

        for email, excepted in sample_emails:
            user = get_user_model().objects.create_user(email, 'testpassword')
            self.assertEqual(user.email, excepted)

    def test_new_user_without_email_raises_error(self):
        """Test new user registration without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpassword')

    def test_create_superuser(self):
        """Test create a superuser."""
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'testpassword',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)