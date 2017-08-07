from selenium import webdriver
import unittest

class NewProjectTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def test_project_setup(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')