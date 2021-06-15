from unittest import TestCase
from market.models import Item

class TestItemModel(TestCase):
    def test_item_model(self):
        # test item model creates item object 
        item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop')
        self.assertEqual(item.name, 'laptop')
        self.assertEqual(item.price, 5000)
        self.assertEqual(item.barcode, 'YT789990')
        self.assertEqual(item.description, 'YT laptop')