from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# tests are organized into classes
# which inherit from unittest.TestCase
class NewVisitorTest(unittest.TestCase):
    # setUp is a function run before
    # all tests, kind of like a try
    def setUp(self):
        self.browser = webdriver.Firefox()
    # tearDown is a function run after
    # all tests, kind of like an except   
    def tearDown(self):
        self.browser.quit()
    
    # methods that start with 'test' are tests
    def test_can_start_list_and_retrieve_later(self):
        # first, get the webpage
        self.browser.get('http://localhost:8000')
        
        # notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # user types "Buy peacock features" into a text box
        inputbox.send_keys('Buy peacock feathers')
        time.sleep(1)

        # user hits enter, and the page updates, now the page
        # lists "1: buy peacock feathers" as an item in
        # the to-do list table
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        # forcing fail to be invoked, can be used to 
        # output message after all tests passed
        self.fail('Finish the Test')

if __name__ == "__main__":
    unittest.main(warnings='ignore')