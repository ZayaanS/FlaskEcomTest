from tests.base_test import BaseTest, db
from market.models import User
from flask import request
from flask_login import current_user

class LoginTest(BaseTest):
    # test login success with valid details
    def test_login_success(self):
        with self.app:
            # register user
            self.app.post('/register', data=dict(username='test', email_address='test@gmail.com', password1='test123', password2='test123'))
            # assert user exists in db
            user = db.session.query(User).filter_by(username='test').first()
            self.assertIsNotNone(user)
            # logout user
            self.app.get('/logout')
            # login user with valid details
            response = self.app.post('/login', data=dict(username='test', password='test123'), follow_redirects=True)
            # assert user is logged in
            self.assertIn(b'Success! You are logged in', response.data)
            self.assertEqual(current_user.get_id(), '1')
            # assert redirects to market
            self.assertIn('/market', request.url)

    # test login error with invalid email
    def test_login_error_email(self):
        # register user
        self.app.post('/register', data=dict(username='test', email_address='test@gmail.com', password1='test123', password2='test123'))
        # assert user exists in db
        user = db.session.query(User).filter_by(username='test').first()
        self.assertIsNotNone(user)
        # logout user
        self.app.get('/logout')
        # login user with invalid username
        response = self.app.post('/login', data=dict(username='tester', password='test123'), follow_redirects=True)
        # assert user is not logged in
        self.assertIn(b'Username and password are not match! Please try again', response.data)
        self.assertIsNone(current_user)

    # test login error with invalid password
    def test_login_error_password(self):
        # register user
        self.app.post('/register', data=dict(username='test', email_address='test@gmail.com', password1='test123', password2='test123'))
        # assert user exists in db
        user = db.session.query(User).filter_by(username='test').first()
        self.assertIsNotNone(user)
        # logout user
        self.app.get('/logout')
        # login user with invalid password
        response = self.app.post('/login', data=dict(username='test', password='testerrr123'), follow_redirects=True)
        # assert user is not logged in
        self.assertIn(b'Username and password are not match! Please try again', response.data)
        self.assertIsNone(current_user)