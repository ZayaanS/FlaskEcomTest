from tests.base_test import BaseTest, db
from market.models import Item

class ItemCrudTest(BaseTest):
    def test_item_model_crud(self):
        with self.app:
            with self.app_context:
                item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop')

                # assert that item does not exist before saving to db
                self.assertIsNone(db.session.query(Item).filter_by(name='laptop').first())

                # assert that item exists after saving to db
                db.session.add(item)
                db.session.commit()
                self.assertIsNotNone(db.session.query(Item).filter_by(name='laptop').first())

                # assert that item does not exist after deleting from database
                db.session.delete(item)
                db.session.commit()
                self.assertIsNone(db.session.query(Item).filter_by(name='laptop').first())

