import random

class DataGenerator:
    def generate_dataset(self, size=131072):  # This is a large dataset
        # Add progress indicator
        print(f"Generating {size} unique 8-digit strings...")
        numbers = set()
        while len(numbers) < size:
            if len(numbers) % 10000 == 0:  # Show progress every 10000 numbers
                print(f"Generated {len(numbers)} numbers...")
            num = f"{random.randint(10000000, 99999999)}"
            numbers.add(num)
        
        numbers = list(numbers)
        mid = size // 2
        return numbers, numbers[:mid], numbers[mid:]

    @staticmethod
    def verify_unique(values):
        """Verify all values are unique"""
        return len(values) == len(set(values))

    def verify_dataset(self, dataset):
        """Verify dataset has unique 8-digit strings"""
        if len(dataset) != len(set(dataset)):
            return False
        return all(s.isdigit() and len(s) == 8 for s in dataset)