from hash_table import HashTable

def test_basic_insert_and_find():
    """Test case 1: Add 5 strings, verify presence and absence"""
    print("\n=== Test Case 1: Basic Insert and Find ===")
    ht = HashTable(initial_size=16, load_factor=0.75, resize_strategy=1)
    
    # Test strings
    strings_to_add = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"Adding {len(strings_to_add)} strings:", ", ".join(strings_to_add))
    
    # Insert strings
    for string in strings_to_add:
        ht.insert(string)
    
    # Verify all strings are found
    print("\nVerifying inserted strings:")
    print("-" * 40)
    all_found = True
    for string in strings_to_add:
        found = ht.find(string)
        status = "✓" if found else "✗"
        print(f"{status} {string}: {'Found' if found else 'Not Found'}")
        all_found &= found
    
    # Test non-existent strings
    non_existent = ["fig", "grape", "honeydew", "kiwi", "lemon"]
    print("\nVerifying non-existent strings:")
    print("-" * 40)
    all_not_found = True
    for string in non_existent:
        found = ht.find(string)
        status = "✓" if not found else "✗"
        print(f"{status} {string}: {'Not Found (correct)' if not found else 'Found (incorrect)'}")
        all_not_found &= not found
    
    assert all_found, "Failed to find all inserted strings"
    assert all_not_found, "Found strings that shouldn't exist"

def test_resize_double_strategy():
    """Test cases 2 & 3: Verify resize with doubling strategy"""
    # Test case 2: 23 values (one resize)
    print("\n=== Test Case 2: Resize Strategy (Double) - 23 values ===")
    ht = HashTable(initial_size=16, load_factor=0.75, resize_strategy=1)
    initial_size = ht.size
    
    for i in range(23):
        ht.insert(f"string{i}")
    
    print(f"Initial size: {initial_size}")
    print(f"Current size: {ht.size}")
    print(f"Resize count: {1 if ht.size > initial_size else 0}")
    
    # Verify all strings are found
    all_found = all(ht.find(f"string{i}") for i in range(23))
    print(f"All 23 strings found: {'✓' if all_found else '✗'}")
    assert all_found, "Failed to find all 23 strings"
    assert ht.size == 32, "Incorrect table size after resize"

    # Test case 3: 24 values (should trigger two resizes)
    print("\n=== Test Case 3: Resize Strategy (Double) - 24 values ===")
    ht = HashTable(initial_size=16, load_factor=0.75, resize_strategy=1)
    initial_size = ht.size
    sizes = [initial_size]
    
    print(f"Initial size: {initial_size}")
    print("Inserting strings and tracking resizes...")
    print("-" * 40)
    
    # Insert strings and track resizes
    for i in range(24):
        current_size = ht.size
        current_count = ht.count
        current_load = current_count / current_size
        
        print(f"Inserting string{i}: count={current_count}, size={current_size}, load={current_load:.3f}")
        ht.insert(f"string{i}")
        
        if ht.size != current_size:
            print(f"Resize triggered at {current_count + 1} items:")
            print(f"  Size changed from {current_size} to {ht.size}")
            sizes.append(ht.size)
    
    resize_count = len(sizes) - 1
    print(f"\nSize progression: {' -> '.join(str(s) for s in sizes)}")
    print(f"Number of resizes: {resize_count}")
    print(f"Final size: {ht.size}")
    print(f"Final count: {ht.count}")
    print(f"Current load factor: {ht.count/ht.size:.3f}")
    
    
    # Verify all strings are found
    found_strings = [ht.find(f"string{i}") for i in range(24)]
    all_found = all(found_strings)
    print(f"All 24 strings found: {'✓' if all_found else '✗'}")
    
    # Verify resize occurred at correct points
    assert 32 in sizes, "First resize to 32 did not occur"
    assert 64 in sizes, "Second resize to 64 did not occur"
    assert resize_count == 2, f"Expected two resizes, got {resize_count}"
    assert all_found, "Failed to find all 24 strings"

def test_resize_addition_strategy():
    """Test case 4: Verify resize with addition strategy"""
    print("\n=== Test Case 4: Resize Strategy (Add 10000) ===")
    ht = HashTable(initial_size=16, load_factor=0.75, resize_strategy=2)
    initial_size = ht.size
    
    # Insert 23 strings
    for i in range(23):
        ht.insert(f"string{i}")
    
    print("After 23 insertions:")
    print(f"Initial size: {initial_size}")
    print(f"Current size: {ht.size}")
    assert ht.size == initial_size + 10000, "Incorrect table size after first resize"
    
    # Insert 24th string
    ht.insert("string23")
    print("\nAfter 24th insertion:")
    print(f"Final size: {ht.size}")
    
    # Verify all strings are found
    all_found = all(ht.find(f"string{i}") for i in range(24))
    print(f"All 24 strings found: {'✓' if all_found else '✗'}")
    assert all_found, "Failed to find all 24 strings"

if __name__ == "__main__":
    print("=== Starting Hash Table Tests ===")
    test_basic_insert_and_find()
    test_resize_double_strategy()
    test_resize_addition_strategy()
    print("\n=== All Tests Completed Successfully! ===")