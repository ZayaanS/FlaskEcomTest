from tests.base_test import BaseTest

class LoginRouteTest(BaseTest):
    def login_route_test(self):
        # test login route returns login page
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            # assert route returns page
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)