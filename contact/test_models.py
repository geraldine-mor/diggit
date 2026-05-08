from django.test import TestCase
from .models import Message


class TestMessageModel(TestCase):

    def setUp(self):
        self.message = Message(
            name="John Smith",
            email="john@smith.com",
            message="Test message"
        )
        self.message.save()

    def test_str_method(self):
        """
        Test that the model's __str__() method returns the message
        """
        message_str = "Test message"
        self.assertEqual(message_str, str(self.message))

    def test_read_defaults_false(self):
        """
        Test that the read field defaults to False
        """
        self.assertFalse(self.message.read)
