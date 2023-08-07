import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
    self.assertEqual(getDataPoint(quote), expected_result)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quote = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
    self.assertEqual(getDataPoint(quote), expected_result)


  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_invalidQuote(self):
        quote = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'GHI'}
        expected_result = (quote['stock'], None, None, None)
        self.assertEqual(getDataPoint(quote), expected_result)

  def test_getDataPoint_invalidQuote(self):
    quote = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'GHI'}
    expected_result = (quote['stock'], None, None, None)
    self.assertEqual(getDataPoint(quote), expected_result)

  def test_getDataPoint_missingKeys(self):
    quote = {'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'PQR', 'top_bid': {'price': 120.48, 'size': 109}, 'top_ask': {'price': 121.2, 'size': 36}}
    expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
    self.assertEqual(getDataPoint(quote), expected_result)

  def test_getDataPoint_negativePrice(self):
        quote = {'top_ask': {'price': -5.0, 'size': 8}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 10.0, 'size': 15}, 'id': '0.109974697771', 'stock': 'MNO'}
        expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
        self.assertEqual(getDataPoint(quote), expected_result)
if __name__ == '__main__':
    unittest.main()





