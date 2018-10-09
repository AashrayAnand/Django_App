from django.test import TestCase
from lists.models import Item, List
# Create your tests here.

# adding new Item to existing list
class NewItemTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, correct_list)
    
    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new list item'})

        self.assertRedirects(response, f'/lists/{correct_list.id}/')
# adding new items to the list 
class NewListTest(TestCase):

    # test to determine if a POST request can be saved
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # check if item added for above POST request
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    # test if a POST request results in a 302 redirect
    def test_redirects_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # ensure the correct status code is sent in the POST response
        # additionally, POST request should redirect to the '/lists/.../' URL mapping
        # so we ensure that the response location is properly set to that value
        new_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/lists/{new_list.id}/')

# class of tests for the list view
class ListViewTest(TestCase):

    def test_uses_list_template(self):
        # test to ensure that the list endpoint is
        # using the correct HTML template,
        # also test to ensure that each list has a unique ID
        # denoted by the auto-generated unique ID for the List
        # object
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')
    # the below test determines if the current list is only displaying
    # items that are a part of that list
    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        # create two objects
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        # create another list, we will be checking if the response
        # doesn't contain this Lists' items, and thus is only showing
        # items for the correct list
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
        # execute GET request
        response = self.client.get(f'/lists/{correct_list.id}/')
        # check if items exist in the list
        self.assertContains(response, 'itemey 2')
        self.assertContains(response, 'itemey 1')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')
    
    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)


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

    # test if a GET request will result in no Item being created and saved
    def test_only_save_item_if_necessary(self):
        self.client.get('/')
        self.assertEquals(Item.objects.count(), 0)

# class of tests for Django object relational mapper
# used to test List and Item model functionality,
# this could be considered an integration test,
# since it is reliant on an outside service (SQLite)
class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        # creating a record in a database is as easy as
        # creating an instance of the Item class, setting
        # attributes, and saving it
    
        # create and save a record in the List
        # database model
        list_ = List()
        list_.save()

        # create and save a record in the Item
        # database model
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()
        # create and save another Item
        second_item = Item()
        second_item.text = 'The second (ever) list item'
        second_item.list = list_
        second_item.save()

        # test that List was created and saved
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        # test that Items were created and saved
        saved_items = Item.objects.all()
        self.assertEquals(saved_items.count(), 2)

        # test that the text attributes for the two Items that were
        # created, as well as their list attributes, are correct
        self.assertEquals(saved_items[0].text, 'The first (ever) list item')
        self.assertEquals(saved_items[0].list, list_)
        self.assertEquals(saved_items[1].text, 'The second (ever) list item')
        self.assertEquals(saved_items[1].list, list_)

