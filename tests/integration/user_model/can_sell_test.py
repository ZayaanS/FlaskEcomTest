from flask import request
from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestCanSellMethod(BaseTest):
    # test can sell user method
    def test_can_sell_method(self):
        with self.app:
            with self.app_context:
                # register user1
                response1 = self.app.post('/register', data=dict(username="Joey", email_address="joey@gmail.com", password1="passme123", password2="passme123",), follow_redirects=True)
                # register user2
                response2 = self.app.post('/register', data=dict(username="Jane", email_address="jane@gmail.com", password1="passme12345", password2="passme12345",), follow_redirects=True)
                # assert users exists in db
                user1 = db.session.query(User).filter_by(username="Joey").first()
                self.assertIsNotNone(user1)
                user2 = db.session.query(User).filter_by(username="Jane").first()
                self.assertIsNotNone(user2)
                # save item to the db
                laptop = Item(name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=1)
                db.session.add(laptop)
                db.session.commit()
                laptop_exists = db.session.query(Item).filter_by(name='laptop').first()
                self.assertTrue(laptop_exists)
                # assert user can sell item
                self.assertEqual(user1.items, [laptop])
                self.assertEqual(user2.items, [])
                self.assertTrue(user1.can_sell(laptop))
                self.assertFalse(user2.can_sell(laptop))
                
                