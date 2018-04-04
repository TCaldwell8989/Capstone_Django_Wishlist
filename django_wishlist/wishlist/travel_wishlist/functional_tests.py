import selenium
from selenium import webdriver

from django.test import LiveServerTestCase


class TitleTest(LiveServerTestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Wishlist' in self.browser.title

class FunctionalityTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.broswer = webdriver.Firefox()
        self.broswer.implicitly_wait(3)

    def tearDown(self):
        self.broswer.quit()

    def test_add_new_place(self):

        # Load home page
        self.broswer.get(self.live_server_url)
        # find input text box
        input_name = self.broswer.find_element_by_id('id_name') # These ids are generated by Django forms
        # Enter place name
        input_name.send_keys('Denver')
        # Find the add button
        add_button = self.broswer.find_element_by_id('add-new-place')
        # And click it
        add_button.click()

        # Got to make this test code wait for page to reload
        # Wait for new element to appear on page
        wait_for_denver = self.broswer.find_element_by_id('place-name-5')

        # Assert places from test_places are on page
        assert 'Tokyo' in self.broswer.page_source
        assert 'New York' in self.broswer.page_source

        # And the new place too
        assert 'Denver' in self.broswer.page_source