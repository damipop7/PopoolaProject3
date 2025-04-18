import random

class DataGenerator:
    @staticmethod
    def generate_dataset(size=131072):
        """Generate unique 8-digit strings"""
        numbers = set()
        while len(numbers) < size:
            num = f"{random.randint(10000000, 99999999)}"
            numbers.add(num)
        
        numbers = list(numbers)
        mid = size // 2
        return numbers, numbers[:mid], numbers[mid:]

    @staticmethod
    def verify_unique(values):
        """Verify all values are unique"""
        return len(values) == len(set(values))