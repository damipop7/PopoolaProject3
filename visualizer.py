import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    @staticmethod
    def plot_rehash_timing(q_values, results):
        plt.figure(figsize=(10, 6))
        plt.plot(q_values, results['no_rehash'], 'o-', label='No Rehash')
        plt.plot(q_values, results['double'], 's-', label='Double Size')
        plt.plot(q_values, results['add_10000'], '^-', label='Add 10000')
        plt.xlabel('q (table size = 2^q)')
        plt.ylabel('Average Time per Insert (seconds)')
        plt.title('Hash Table Performance vs Table Size')
        plt.legend()
        plt.grid(True)
        plt.savefig('rehash_timing.png')
        plt.close()

    def plot_load_factor_timing(self, load_factors, results, Q):
        plt.figure(figsize=(12, 8))
        lambda_vals = np.linspace(0, 0.99, 100)
        
        # Theoretical curves
        linear_succ = [0.5 * (1 + 1/(1-x)) for x in lambda_vals]
        double_succ = [0.5 * (1/(1-x)) for x in lambda_vals]
        measured_succ = [Q*x for x in results['successful']]
        
        plt.plot(lambda_vals, linear_succ, 'b-', label='Linear Probing (Theory)')
        plt.plot(lambda_vals, double_succ, 'g-', label='Double Hashing (Theory)')
        plt.plot(load_factors, measured_succ, 'ro', label='Measured')
        
        plt.xlabel('Load Factor (λ)')
        plt.ylabel('Average Probes')
        plt.title('Hash Table Performance vs Load Factor')
        plt.legend()
        plt.grid(True)
        plt.savefig('time_succ.png')
        plt.close()