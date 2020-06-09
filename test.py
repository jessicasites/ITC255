import unittest
from classcode import classcode 

class CustomerTest(unittest,TestCase):

   def setUp(self):
        self.Customer=Customer('1', 'Smith','John', 'johnsmith@gmail.com')

    def test_getCustomerID(self):
        self.assertEqual(str(self.Customer.getCustomerID()),'1')

    def test_CustomerString(self):
        self.assertEqual(str(self.Customer.getLastName()),'Smith')

    def test_getFirstName(self):
        self.assertEqual(str(self.Customer.getFirstName()),'John')
    
    def test_getPhone(self):
        self.assertEqual(str(self.Customer.getPhone()),'johnsmith@gmail.com')

class ItemTest(unittest,TestCase):
    def setUp(self):
        self.item=Item('1','soap','5.00','hand soap')

    def test_getItemID(self):
        self.assertEqual(str(self.Item.getItemID()),'1')

    def test_itemString(self):
        self.assertEqual(str(self.Item.getItemName()),'soap')

    def test_getitemPrice(self):
        self.assertEqual(str(self.Item.getPrice()), '5.00')

    def test_getitemDesc(self):
        self.assertEqual(str(self.Item.Desc()),'hand soap')

class SaleTest(unittest,TestCase):
    def setUp(self):
        self.item=Item('1','soap','5.00')

    def test_getsaleID(self):
        self.assertEqual(str(self.Sale.getItemID()),'1')

    def test_itemString(self):
        self.assertEqual(str(self.Sale.getItems()),'soap')

    def test_getTotal(self):
        self.assertEqual(str(self.Sale.getTotal()), '5.00')

