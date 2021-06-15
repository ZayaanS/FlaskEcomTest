from flask_sqlalchemy.utils import parse_version
from tests.base_test import BaseTest, db
from market.models import Item, User
from flask_login import current_user

class TestSellingItem(BaseTest):

    def test_selling_item_success(self):
        # test selling an item if user owns item
        with self.app:
            with self.app_context:
                
                # create user
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)
                
                # assert user is logged in
                self.assertEqual(current_user.get_id(), '1')

                # assert user budget is 1000
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(user.budget, 1000)
                
                # add item to db
                item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=1)
                db.session.add(item)
                db.session.commit()
                
                # assert item exists
                item_exists = db.session.query(Item).filter_by(name='laptop').first()
                self.assertTrue(item_exists)
               
                # assert user owns item
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(user.items, [item])
                self.assertEqual(item.owner, 1)

                # sell item to market
                response = self.app.post('/market', data=dict(sold_item='laptop') , follow_redirects=True)

                # assert item is not owned
                self.assertIn(b'Congratulations! You sold laptop back to market!', response.data)
                self.assertEqual(user.items, [])
                self.assertIsNone(item.owner)
                
                # assert user budget increased
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(user.budget, 6000)


    def test_selling_item_error(self):
        # test selling an item if user does not own item
        with self.app:
            with self.app_context:
                
                # create user
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)
                
                # assert user is logged in
                self.assertEqual(current_user.get_id(), '1')

                # assert user budget is 1000
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(user.budget, 1000)
                
                # add item to db with owner id 34
                item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=34)
                db.session.add(item)
                db.session.commit()
                
                # assert item exists
                item_exists = db.session.query(Item).filter_by(name='laptop').first()
                self.assertTrue(item_exists)
               
                # assert owner id is 34
                self.assertEqual(item_exists.owner, 34)

                # sell item to market
                response = self.app.post('/market', data=dict(sold_item='laptop') , follow_redirects=True)

                # assert item cannot be sold
                self.assertIn(b'Something went wrong with selling laptop', response.data)
                
                # assert user budget does not increase
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertEqual(user.budget, 1000)


    

