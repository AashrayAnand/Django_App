from selenium import webdriver
import unittest

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
        
        # check browser title is To-Do
        self.assertIn('To-Do', self.browser.title)
        
        # forcing fail to be invoked, can be used to 
        # output message after all tests passed
        self.fail('Finish the Test')

if __name__ == "__main__":
    unittest.main(warnings='ignore')