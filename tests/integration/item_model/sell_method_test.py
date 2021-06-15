from tests.base_test import BaseTest, db
from market.models import Item, User
from flask_login import current_user

class TestSellMethod(BaseTest):
    def test_sell_method(self):
        # test sell method works as expected
        with self.app:
            with self.app_context:
                
                # create user
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)
                
                # assert user is logged in
                self.assertEqual(current_user.get_id(), '1')
                
                # add item to db with user 1 being owner
                item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=1)
                db.session.add(item)
                db.session.commit()
                
                # assert item exists
                item_exists = db.session.query(Item).filter_by(name='laptop').first()
                self.assertTrue(item_exists)

                # assert user owns item
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(item_exists.owner, user.id) 

                # assert user current budget is 1000
                self.assertEqual(user.budget, 1000)
               
                # use sell method
                item_exists.sell(user)

                # assert owner is none
                soldItem = db.session.query(Item).filter_by(name='laptop').first()
                self.assertIsNone(soldItem.owner)

                # assert user budget increased
                self.assertEqual(user.budget, 6000)
