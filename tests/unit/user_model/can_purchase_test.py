from unittest import TestCase
from market.models import User, Item

class TestCanPurchase(TestCase):
    def test_can_purchase(self):
        # test can purchase method of user model
        user1 = User(id=25, username='Honey', email_address='honey@email.com', password_hash='passme123', budget=7000)
        user2 = User(id=26, username='Bob', email_address='bob@email.com', password_hash='passme12345', budget=4000)
        item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=27)
        self.assertTrue(user1.can_purchase(item))
        self.assertFalse(user2.can_purchase(item))