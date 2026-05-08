from django.test import TestCase
from .forms import MessageForm


class TestMessageForm(TestCase):

    def test_form_is_validated(self):
        """
        Test that the form is valid when all fields are correctly filled
        """
        message_form = MessageForm(
            {'name': 'John Smith',
            'email': 'js@email.com',
            'message': 'Hello, test message'}
        )
        self.assertTrue(message_form.is_valid())

    def test_name_validation(self):
        """
        Test that missing name field causes the form to be invalid
        """
        message_form = MessageForm(
            {'name': '',
            'email': 'js@email.com',
            'message': 'Hello, test message'}
        )
        self.assertFalse(message_form.is_valid())

    def test_name_length_validation(self):
        """
        Test that names longer than 30 characters cause
        the form to be invalid
        """
        message_form = MessageForm(
            {'name': 'Jonathan Richard Jefferson-Smith',
            'email': 'js@email.com',
            'message': 'Hello, test message'}
        )
        self.assertFalse(message_form.is_valid())

    def test_email_validation(self):
        """
        Test that missing email field causes the form to be invalid
        """
        message_form = MessageForm(
            {'name': 'John Smith',
            'email': '',
            'message': 'Hello, test message'}
        )
        self.assertFalse(message_form.is_valid())

    def test_email_type_validation(self):
        """
        Test that malformed emails cause the form to be invalid
        """
        message_form = MessageForm(
            {'name': 'John Smith',
             'email': 'john_smith',
             'message': 'Hello, test message'}
        )
        self.assertFalse(message_form.is_valid())

    def test_message_validation(self):
        """
        Test that missing message field causes the form to be invalid
        """
        message_form = MessageForm(
            {'name': 'John Smith',
             'email': 'john_smith',
             'message': ''}
        )
        self.assertFalse(message_form.is_valid())