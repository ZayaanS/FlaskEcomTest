from tests.base_test import BaseTest, db
from market.models import Item, User
from flask_login import current_user

class TestBuyMethod(BaseTest):
    def test_buy_method(self):
        # test buy method works as expected
        with self.app:
            with self.app_context:
                
                # create user
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)
                
                # assert user is logged in
                self.assertEqual(current_user.get_id(), '1')
                
                # add item to db
                item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=25)
                db.session.add(item)
                db.session.commit()
                
                # assert item exists
                item_exists = db.session.query(Item).filter_by(name='laptop').first()
                self.assertTrue(item_exists)
               
                # update user budget
                user = db.session.query(User).filter_by(username='chibi').first()
                user.budget = 7000
                db.session.commit()
                chibi = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(chibi.budget, 7000)
                
                # use buy method
                item_exists.buy(chibi)

                # assert user owns item
                ownedItem = db.session.query(Item).filter_by(name='laptop').first()
                self.assertEqual(ownedItem.owner, chibi.id)

                # assert user budget changed
                self.assertEqual(chibi.budget, 2000)
