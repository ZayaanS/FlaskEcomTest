from unittest import TestCase
from market.models import User

class UserModelTest(TestCase):
    # test user model creates user object
    def test_user_creation(self):
        new_user = User(id=1, username='Kate', email_address='kate@gmail.com', password_hash='#&*565&*&&^489846&*^%%$', budget=200000)
        self.assertEqual(new_user.id, 1)
        self.assertEqual(new_user.username, 'Kate')
        self.assertEqual(new_user.password_hash, '#&*565&*&&^489846&*^%%$')
        self.assertEqual(new_user.budget, 200000)
        
