import random

class DataGenerator:
    @staticmethod
    def generate_unique_strings(size=131072):
        """Generate unique 8-digit strings"""
        numbers = set()
        while len(numbers) < size:
            num = str(random.randint(10000000, 99999999))
            numbers.add(num)
        
        numbers = list(numbers)
        # Split into add and check values
        add_values = numbers[:size//2]
        check_values = numbers[size//2:]
        return numbers, add_values, check_values

    @staticmethod
    def verify_unique(values):
        """Verify all values are unique"""
        return len(values) == len(set(values))