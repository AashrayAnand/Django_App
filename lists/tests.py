from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

# class of tests for the home page ("/")
class HomePageTest(TestCase):
    
    # test to determine if we can resolve the root of
    # the site ("/") to a particular view function
    def test_root_url_resolves_to_home_page(self):
        # function used internally to resolve URLs
        # and find the view function they map to
        found = resolve('/')
        # checking that the view function found
        # is the home_page view function
        self.assertEqual(found.func, home_page)
    # test to determine if the root of the site
    # returns the correct HTML output
    def test_root_url_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

