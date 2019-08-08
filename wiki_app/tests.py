from django.test import TestCase, Client
from .views import load_suggestion, homepage, get_article
from django.urls import reverse

client = Client()

class ProjectViewTests(TestCase):
    """
    Class to test the views used in the project
    """
    def test_home_page(self):
        response = client.get(reverse('home_view'))
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        """
        Test to check the load_suggestion view is working
        correctly or not by checking for the inclusion of
        expected keywords in the response
        """
        response = client.get(reverse('search_view'), {"search_word":"quora"})
        self.assertContains(response, 'quora')

    def test_search_view_no_input(self):
        """
        Test to check whether the view calling the wiki API
        with no input returns empty list or not
        """
        response = client.get('/wiki_app/search/', {'search_word':''})
        self.assertEqual(response.status_code, 200)

    def test_get_article_no_input(self):
        """
        Test to check whether the get_article view is responding
        with a message for empty input
        """
        response = client.get(reverse('get_article'), {"article":""})
        self.assertEqual(response.content, b'Please provide an valid name get wiki data')