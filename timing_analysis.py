import time
import numpy as np
from hash_table import HashTable
from data_generator import DataGenerator

class TimingAnalysis:
    def __init__(self):
        """Initialize the timing analysis with data generator"""
        self.data_gen = DataGenerator()
        _, self.add_values, self.check_values = self.data_gen.generate_unique_strings()

    def time_rehash_strategies(self, q_values=range(4, 18)):
        """
        Time the performance of different rehashing strategies
        """
        results = {
            'no_rehash': [],
            'double': [],
            'add_10000': []
        }

        for q in q_values:
            size = 2**q
            num_values = int((3/4) * size - 1)
            values_to_insert = self.add_values[:num_values]

            # No rehash (large initial size)
            ht = HashTable(2**17, 0.75, 1)
            start = time.perf_counter()
            for value in values_to_insert:
                ht.insert(value)
            results['no_rehash'].append((time.perf_counter() - start) / num_values)

            # Double strategy
            ht = HashTable(2**q, 0.75, 1)
            start = time.perf_counter()
            for value in values_to_insert:
                ht.insert(value)
            results['double'].append((time.perf_counter() - start) / num_values)

            # Add 10000 strategy
            ht = HashTable(2**q, 0.75, 2)
            start = time.perf_counter()
            for value in values_to_insert:
                ht.insert(value)
            results['add_10000'].append((time.perf_counter() - start) / num_values)

        return results

    def time_load_factors(self, table_size=65536):
        """
        Time performance vs load factor
        """
        load_factors = np.linspace(0.1, 0.99, 30)
        results = {
            'successful': [],
            'unsuccessful': []
        }

        for load_factor in load_factors:
            ht = HashTable(table_size, 1.0, 1)  # Using load_factor=1.0 to prevent resizing
            num_to_insert = int(table_size * load_factor)
            
            # Insert values up to desired load factor
            for i in range(num_to_insert):
                ht.insert(self.add_values[i])

            # Time successful searches
            start = time.perf_counter()
            for i in range(num_to_insert):
                ht.find(self.add_values[i])
            succ_time = (time.perf_counter() - start) / num_to_insert
            results['successful'].append(succ_time)

            # Time unsuccessful searches
            start = time.perf_counter()
            for i in range(num_to_insert):
                ht.find(self.check_values[i])
            unsucc_time = (time.perf_counter() - start) / num_to_insert
            results['unsuccessful'].append(unsucc_time)

        return load_factors, results

    def save_results(self, results, filename):
        """Save timing results to a file"""
        with open(filename, 'w') as f:
            for strategy, times in results.items():
                f.write(f"{strategy}:\n")
                for i, time in enumerate(times):
                    f.write(f"  q={i+4}: {time:.6f}\n")