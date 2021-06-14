from unittest import TestCase
from market.models import User

class PrettierBudgetTest(TestCase):
    def test_prettier_budget(self):
        # test prettier_budget method works as expected
        budget = User(id=1, username='Kate', email_address='kate@gmail.com', password_hash='#&*565&*&&^489846&*^%%$', budget=200000).prettier_budget
        self.assertEqual(budget, '200,000$')
        