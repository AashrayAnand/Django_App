from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

# fixes the settings issue when using LiveServerTestCase
# should refactor this later
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
django.setup()

import unittest
import time

from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10

# tests are organized into classes
# which inherit from unittest.TestCase
class NewVisitorTest(LiveServerTestCase):
    # setUp is a function run before
    # all tests, kind of like a try
    def setUp(self):
        self.browser = webdriver.Firefox()
    # tearDown is a function run after
    # all tests, kind of like an except   
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            # unless content hasn't loaded
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # methods that start with 'test' are tests
    def test_can_start_list_and_retrieve_later(self):
        # first, get the webpage
        self.browser.get(self.live_server_url)
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
        # user hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        # user hits enter, and the page updates, now the page
        # lists "1: buy peacock feathers" as an item in
        # the to-do list table
        self.wait_for_row_in_list_table(row_text='1: Buy peacock feathers')
        # add another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(row_text='1: Buy peacock feathers')
        self.wait_for_row_in_list_table(row_text='2: Use peacock feathers to make a fly')
        # forcing fail to be invoked, can be used to 
        # output message after all tests passed
    def test_succeeded_all(self):
        self.fail('============= Finish the Test =============')
if __name__ == "__main__":
    unittest.main(warnings='ignore')