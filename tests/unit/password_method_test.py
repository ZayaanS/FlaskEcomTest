from unittest import TestCase
from market.models import User

class PasswordMethodTest(TestCase):
   # testing password getter method
    def test_password_method(self):
        new_user = User(id=1, username='Kate', email_address='kate@gmail.com', password_hash='6465161485u$%#%^&%^&*^*(&*(pa^&%^&*IY*(%^##$%^ss1%$&*^&*23456', budget=200000)
        password = new_user.password
        self.assertEqual(password, '6465161485u$%#%^&%^&*^*(&*(pa^&%^&*IY*(%^##$%^ss1%$&*^&*23456')
        