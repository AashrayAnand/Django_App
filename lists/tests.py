from django.test import TestCase

# Create your tests here.

# class of tests for the home page ("/")
class HomePageTest(TestCase):
    
    # utilizing the django test client, we can fetch the response
    # from a provided URL parameter in this case, the root of the 
    # site, also we can determine if the correct HTML template is 
    # rendered by the subsequent view function, therefore this
    # test checks both if the root url resolves, and if
    # it renders the correct content
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    # alternatively, we can create an HttpRequest object, call the
    # home_page view function with the request as parameter, and check
    # the same assertion (self.client.get executes this all in one step) 

    # test to determine if a POST request can be saved
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

