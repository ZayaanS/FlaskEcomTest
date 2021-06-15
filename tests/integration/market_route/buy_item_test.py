from flask_sqlalchemy.utils import parse_version
from tests.base_test import BaseTest, db
from market.models import Item, User
from flask_login import current_user

class TestBuyItem(BaseTest):
    def test_buying_item_success(self):
        # test buying an item if user has enough budget
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

                # purchase item from market
                response = self.app.post('/market', data=dict(purchased_item='laptop') , follow_redirects=True)

                # assert item is purchased
                self.assertIn(b'Congratulations! You purchased laptop for 5000$', response.data)


