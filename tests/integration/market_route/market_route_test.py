from tests.base_test import BaseTest

class TestMarketRoute(BaseTest):
    def test_market_route(self):
        # test market route while not signed in
        with self.app:
            response = self.app.get('/market', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please log in to access this page', response.data)

    def test_market_route_signedin(self):
        # test market route while signed in
        with self.app:
            self.app.post('/register', data=dict(username='namey', email_address='namey@mail.com', password1='passme123', password2='passme123'), follow_redirects=True)
            response = self.app.get('/market', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Available items on the Market', response.data)