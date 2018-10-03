from django.test import TestCase
from lists.models import Item
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
        self.client.post('/', data={'item_text': 'A new list item'})
        # check if item added for above POST request
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    # test if a POST request results in a 302 redirect
    def test_redirects_after_post(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        # ensure the correct status code is sent in the POST response
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_items(self):
        # create two objects
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        # execute GET request
        response = self.client.get('/')
        # check if items exist in the list
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    # test if a GET request will result in no Item being created and saved
    def test_only_save_item_if_necessary(self):
        self.client.get('/')
        self.assertEquals(Item.objects.count(), 0)

# class of tests for Django object relational mapper
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        # creating a record in a database is as easy as
        # creating an instance of the Item class, setting
        # attributes, and saving it
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second (ever) list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEquals(saved_items.count(), 2)

        self.assertEquals(saved_items[0].text, 'The first (ever) list item')
        self.assertEquals(saved_items[1].text, 'The second (ever) list item')

