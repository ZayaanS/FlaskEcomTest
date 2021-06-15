from unittest import TestCase
from market.models import Item

class TestItemReprMethod(TestCase):
    def test_item_repr(self):
        # test item repr method
        item = Item(id=1, name='laptop', price=5000, barcode='YT789990', description='YT laptop', owner=25)
        self.assertEqual(item.__repr__(), 'Item laptop')