from django.urls import reverse
from django.test import TestCase
from .forms import MessageForm
from .models import Message


class TestContactViews(TestCase):

    def test_render_contact_page(self):
        """
        Test that the contact page renders with contact form
        """
        response = self.client.get(reverse('contact'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['contact_form'], MessageForm)
        
    
    def test_form_submission(self):
        """
        Test for submitting a valid form
        """
        data = {
            'name': 'John Smith',
            'email': 'john@smith.com',
            'message': "Test message"
        }
        response = self.client.post(
            reverse('contact'), data, follow=True)
        
        self.assertRedirects(
            response,
            '/',
            status_code=302,
            target_status_code=200
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your message has been sent", response.content
        )
