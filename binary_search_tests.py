from binary_search import BinarySearch
import unittest
import json
import time

bs = BinarySearch()

with open("items.json", "r") as file:
    data = json.load(file)

# Setting values to created variables
simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]

# Test cases to test Binary Search algorithm
class BinarySearchTests(unittest.TestCase):

    def setUp(self):
        print (".......... %s" % self._testMethodName)

    def test_iterative_binary_search_with_simple_list(self):
        # ARRANGE
        # You can check the index of each item in the items,json file
        item, expected_index = 3, 1

        # ACT
        # Run the method we created and get the index of the item we were looking for
        index = bs.search_iterative(simple_list, item) # => 1

        # ASSERT
        # Compare the resulting index with the expected index
        self.assertEqual(expected_index, index) # => 1 = 1

if __name__ == '__main__':
    unittest.main()