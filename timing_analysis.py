import time
import numpy as np
from hash_table import HashTable
from data_generator import DataGenerator

class TimingAnalysis:
    def __init__(self):
        self.data_gen = DataGenerator()
        self.whole_list, self.add_values, self.check_values = self.data_gen.generate_dataset()

    def time_rehash_strategies(self, q_values):
        results = {'no_rehash': [], 'double': [], 'add_10000': []}
        
        for q in q_values:
            print(f"\nProcessing q={q}...")
            size = 2**q
            num_values = int((3/4) * size - 1)
            
            if num_values <= 0:
                print(f"Warning: Invalid number of values ({num_values}) for q={q}")
                continue
                
            values = self.whole_list[:num_values]
            if not values:
                print(f"Warning: No values available for processing q={q}")
                continue
                
            for strategy, config in [
                ('no_rehash', (2**17, 0.75, 1)),
                ('double', (2**q, 0.75, 1)),
                ('add_10000', (2**q, 0.75, 2))
            ]:
                print(f"Testing {strategy} strategy...")
                ht = HashTable(*config)
                start = time.perf_counter()
                
                for i, val in enumerate(values):
                    if i % 100 == 0:  # More frequent progress updates
                        print(f"\rInserted {i}/{len(values)} values...", end='', flush=True)
                    ht.insert(val)
                    
                elapsed = time.perf_counter() - start
                results[strategy].append(elapsed / num_values)
                print(f"\nCompleted {strategy} in {elapsed:.2f} seconds")
        
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
        
        self._save_load_factor_results(load_factors, results, 'load_factor_timing.txt')
        return load_factors, results

    def _save_timing_results(self, results, filename):
        """Save timing results to file"""
        with open(filename, 'w') as f:
            f.write("Rehash Timing Results\n")
            f.write("====================\n\n")
            for strategy in ['no_rehash', 'double', 'add_10000']:
                f.write(f"\n{strategy} strategy:\n")
                for i, time in enumerate(results[strategy]):
                    f.write(f"q={i+4}: {time:.6f}\n")

    def _save_load_factor_results(self, load_factors, results, filename):
        with open(filename, 'w') as f:
            f.write("Load Factor Analysis Results\n")
            f.write("===========================\n\n")
            for i, lf in enumerate(load_factors):
                f.write(f"Load Factor: {lf:.3f}\n")
                f.write(f"Successful Search Time: {results['successful'][i]:.6f}\n")
                f.write(f"Unsuccessful Search Time: {results['unsuccessful'][i]:.6f}\n\n")