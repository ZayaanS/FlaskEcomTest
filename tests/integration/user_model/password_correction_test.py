from flask import request
from tests.base_test import BaseTest
from market import db
from market.models import User


class TestPasswordCorrectionMethod(BaseTest):
    # test password correction test
    def test_password_correction_method(self):
        with self.app:
            with self.app_context:
                # register user with password 'passme123'
                response = self.app.post('/register', data=dict(username="JoeDoe", email_address="joe@gmail.com", password1="passme123", password2="passme123",), follow_redirects=True)
                # assert user exists in db
                user = db.session.query(User).filter_by(username="JoeDoe").first()
                self.assertIsNotNone(user)
                # assert user password is hashed       
                self.assertNotEqual(user.password_hash, "passme123")   
                # call correct password method
                unhashed = user.check_password_correction('passme123')
                # assert method returns 'passme123'
                self.assertTrue(unhashed)