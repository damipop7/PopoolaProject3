import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_basic_functionality(self):
        """Test case 1: Add 5 strings, verify presence/absence"""
        ht = HashTable(16, 0.75, 1)
        test_strings = ["test1", "test2", "test3", "test4", "test5"]
        other_strings = ["other1", "other2", "other3", "other4", "other5"]
        
        for s in test_strings:
            ht.insert(s)
            
        for s in test_strings:
            self.assertTrue(ht.find(s))
        for s in other_strings:
            self.assertFalse(ht.find(s))

    def test_resize_double(self):
        """Test cases 2 & 3: Verify resize behavior with doubling strategy"""
        ht = HashTable(16, 0.75, 1)
        
        # Add 23 values
        for i in range(23):
            ht.insert(f"value{i}")
        self.assertEqual(ht.size, 32)  # Verify one resize occurred
        
        # Add 24th value
        ht.insert("value23")
        self.assertEqual(ht.size, 64)  # Verify second resize occurred

    def test_resize_add(self):
        """Test case 4: Verify resize behavior with add strategy"""
        ht = HashTable(16, 0.75, 2)
        
        # Add 23 values
        for i in range(23):
            ht.insert(f"value{i}")
        self.assertEqual(ht.size, 10016)  # Verify correct size after resize

if __name__ == '__main__':
    unittest.main()