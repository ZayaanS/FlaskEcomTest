from flask import request
from tests.base_test import BaseTest
from market import db
from market.models import User


class TestRegister(BaseTest):
    # testing password setter method
    def test_register_new_user(self):
        with self.app:
            with self.app_context:
                # create user in db with post method
                response = self.app.post('/register', data=dict(username="JoeDoe", email_address="joe@gmail.com", password1="202177", password2="202177",), follow_redirects=True)
                # assert user exists in db
                user = db.session.query(User).filter_by(username="JoeDoe").first()
                self.assertIsNotNone(user)
                # assert user password is hashed       
                self.assertNotEqual(user.password_hash, "202177")   