from tests.base_test import BaseTest

class TestHomeRoute(BaseTest):
    def test_home_route(self):
        # test home routes
        with self.app:
            response = self.app.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jim Shaped Coding Market', response.data)

    def test_2nd_home_route(self):
        # test 2nd home route
        with self.app:
            response = self.app.get('/home', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jim Shaped Coding Market', response.data)