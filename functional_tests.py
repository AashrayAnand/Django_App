from selenium import webdriver
import unittest


class visitorTest(unittest.TestCase):
    # set browser
    def setUp(self):
        self.browser = webdriver.Firefox()
    # quit browser    
    def tearDown(self):
        self.browser.quit()
    
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