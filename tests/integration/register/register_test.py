from tests.base_test import BaseTest, db
from market.models import User

class TestRegisterPost(BaseTest):
    def test_register_post_valid(self):
        # test register post with valid details
        with self.app:
            response = self.app.post('/register', data=dict(username='person', email_address='person@gmail.com', password1='passme123', password2='passme123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNotNone(user)

    def test_register_post_password_error(self):
        # test register post with mismatched passwords
        with self.app:
            response = self.app.post('/register', data=dict(username='person', email_address='person@gmail.com', password1='passme123', password2='passmee'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_username_error(self):
        # test register post with short username
        with self.app:
            response = self.app.post('/register', data=dict(username='a', email_address='person@gmail.com', password1='passme123', password2='passme123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='a').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_email_error(self):
        # test register post with invalid email
        with self.app:
            response = self.app.post('/register', data=dict(username='person', email_address='person', password1='passme123', password2='passme123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_password_error_2(self):
        # test register post with short password
        with self.app:
            response = self.app.post('/register', data=dict(username='person', email_address='person@gmail.com', password1='pass', password2='pass'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_no_username(self):
        # test register post with no username
        with self.app:
            response = self.app.post('/register', data=dict(email_address='person@gmail.com', password1='pass', password2='pass'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(email_address='person@gmail.com').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_no_email(self):
        # test register post with no email
        with self.app:
            response = self.app.post('/register', data=dict(username='person', password1='pass', password2='pass'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_no_password1(self):
        # test register post with no password1
        with self.app:
            response = self.app.post('/register', data=dict(username='person',email_address='person@gmail.com', password2='pass123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)

    def test_register_post_no_password2(self):
        # test register post with no password1
        with self.app:
            response = self.app.post('/register', data=dict(username='person',email_address='person@gmail.com', password1='pass123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # assert user is not created in db
            user = db.session.query(User).filter_by(username='person').first()
            self.assertIsNone(user)
            self.assertIn(b'There was an error with creating a user', response.data)


