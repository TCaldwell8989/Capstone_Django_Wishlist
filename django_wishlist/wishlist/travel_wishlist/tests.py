from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestViewHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places']) # Empty lists are false

class TestWishList(TestCase):

    # Load this data into the database for all of the tests in this class
    fixtures = ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was sent to the template?
        data_rendered = list(response.context['places'])
        # What data is in the database? Get all of the items where visited = False
        data_expected = list(Place.objects.filter(visited=False))
        # Is it the same?
        self.assertCountEqual(data_rendered, data_expected)

class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place_to_wishlist(self):

        response = self.client.post(reverse('place_list'), { 'name': 'Tokyo', 'visited': False}, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was used to populate the template?
        response_places = response.context['places']
        # Should be 1 item
        self.assertEqual(len(response_places), 1)