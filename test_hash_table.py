import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_basic_operations(self):
        # Test 1: Add 5 strings and verify
        ht = HashTable(16, 0.75, 1)
        test_strings = ["test1", "test2", "test3", "test4", "test5"]
        other_strings = ["other1", "other2", "other3", "other4", "other5"]
        
        for s in test_strings:
            ht.insert(s)
        
        # Verify all test strings are found
        for s in test_strings:
            self.assertTrue(ht.find(s))
            
        # Verify other strings are not found
        for s in other_strings:
            self.assertFalse(ht.find(s))

    def test_resize_double_strategy(self):
        ht = HashTable(16, 0.75, 1)
        initial_size = ht.size
        
        # Add 23 values (should trigger one resize)
        for i in range(23):
            ht.insert(f"test{i}")
            
        # Verify size doubled once
        self.assertEqual(ht.size, initial_size * 2)
        
        # Add 24th value (should trigger second resize)
        ht.insert("test24")
        self.assertEqual(ht.size, initial_size * 4)
        
        # Verify all values can be found
        for i in range(24):
            self.assertTrue(ht.find(f"test{i}"))

    def test_resize_add_strategy(self):
        ht = HashTable(16, 0.75, 2)
        initial_size = ht.size
        
        # Add 23 values (should trigger one resize)
        for i in range(23):
            ht.insert(f"test{i}")
            
        # Verify size increased by 10000
        self.assertEqual(ht.size, initial_size + 10000)
        
        # Verify all values can be found
        for i in range(23):
            self.assertTrue(ht.find(f"test{i}"))

if __name__ == '__main__':
    unittest.main()