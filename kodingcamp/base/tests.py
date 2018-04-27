from django.test import TestCase, Client

# Create your tests here.
class BaseAppTests(TestCase):

    def test_home_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('hello world' in response.content)