import time
import numpy as np
from hash_table import HashTable
from data_generator import DataGenerator

class TimingAnalysis:
    def __init__(self):
        self.data_gen = DataGenerator()
        self.whole_list, self.add_values, self.check_values = self.data_gen.generate_dataset()

    def time_rehash_strategies(self, q_values=range(4, 18)):  # Changed from time_rehash_cost
        results = {'no_rehash': [], 'double': [], 'add_10000': []}
        
        for q in q_values:
            size = 2**q
            num_values = int((3/4) * size - 1)
            values = self.whole_list[:num_values]
            
            # Time each strategy
            for strategy, config in [
                ('no_rehash', (2**17, 0.75, 1)),
                ('double', (2**q, 0.75, 1)),
                ('add_10000', (2**q, 0.75, 2))
            ]:
                ht = HashTable(*config)
                start = time.perf_counter()
                for val in values:
                    ht.insert(val)
                elapsed = time.perf_counter() - start
                results[strategy].append(elapsed / num_values)
        
        self._save_results(results, 'rehash_timing.txt')
        return results

    def time_load_factors(self):
        load_factors = np.linspace(0.1, 0.99, 30)
        results = {'successful': [], 'unsuccessful': []}
        
        for lf in load_factors:
            # Setup hash table
            ht = HashTable(65536, 1.0, 1)
            num_values = int(65536 * lf)
            
            # Insert values
            for i in range(num_values):
                ht.insert(self.add_values[i])
            
            # Time successful searches
            start = time.perf_counter()
            for i in range(num_values):
                ht.find(self.add_values[i])
            results['successful'].append((time.perf_counter() - start) / num_values)
            
            # Time unsuccessful searches
            start = time.perf_counter()
            for i in range(num_values):
                ht.find(self.check_values[i])
            results['unsuccessful'].append((time.perf_counter() - start) / num_values)
        
        self._save_results(results, 'load_factor_timing.txt')
        return load_factors, results

    def _save_results(self, results, filename):
        """Save timing results to a file"""
        with open(filename, 'w') as f:
            for strategy, times in results.items():
                f.write(f"{strategy}:\n")
                for i, time in enumerate(times):
                    f.write(f"  q={i+4}: {time:.6f}\n")