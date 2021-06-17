from tests.base_test import BaseTest

class TestRegisterRoute(BaseTest):
    def test_register_route(self):
        # test register route returns register page
        with self.app:
            response = self.app.get('/register', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Create your Account', response.data)