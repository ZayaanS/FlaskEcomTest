from tests.base_test import BaseTest, db
from market.models import User
from flask import request
from flask_login import current_user

class LogoutTest(BaseTest):
    # test logout while user is logged in
    def test_logout_success(self):
        with self.app:
            # register user
            self.app.post('/register', data=dict(username='test', email_address='test@gmail.com', password1='test123', password2='test123'), follow_redirects=True)
            # assert user exists in db
            user = db.session.query(User).filter_by(username='test').first()
            self.assertIsNotNone(user)
            # assert user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # logout user
            self.app.get('/logout', follow_redirects=True)
            #assert user is logged out
            self.assertIsNone(current_user.get_id())
            # assert user redirected to home page
            self.assertIn('/home', request.url)

    # test logout while user is not logged in
    def test_logout_success(self):
        with self.app:
            # logout user
            response= self.app.get('/logout', follow_redirects=True)
            #assert error message appears
            self.assertIn(b'You have been logged out', response.data)
            