import random

class DataGenerator:
    def generate_dataset(self, size=131072):
        """Generate unique 8-digit strings"""
        print(f"Generating {size} unique strings...")
        numbers = set()
        while len(numbers) < size:
            if len(numbers) % 10000 == 0:
                print(f"Progress: {len(numbers)}/{size}")
            num = f"{random.randint(10000000, 99999999)}"
            numbers.add(num)
        
        numbers = list(numbers)
        mid = size // 2
        return numbers, numbers[:mid], numbers[mid:]

    def verify_unique(self, values):
        """Verify all values are unique 8-digit strings"""
        if len(values) != len(set(values)):
            return False
        return all(len(s) == 8 and s.isdigit() for s in values)