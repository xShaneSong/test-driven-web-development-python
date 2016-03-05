from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expectd_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expectd_html)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        expectd_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expectd_html)
