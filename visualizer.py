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
        # Plot for successful searches
        plt.figure(figsize=(12, 8))
        lambda_vals = np.linspace(0, 0.99, 100)
        
        # Theoretical curves
        linear_succ = [0.5 * (1 + 1/(1-x)) for x in lambda_vals]
        double_succ = [0.5 * (1/(1-x)) for x in lambda_vals]
        measured_succ = [Q*x for x in results['successful']]
        
        plt.plot(lambda_vals, linear_succ, 'b-', linewidth=2, label='Linear Probing (Theory)')
        plt.plot(lambda_vals, double_succ, 'g-', linewidth=2, label='Double Hashing (Theory)')
        plt.plot(load_factors, measured_succ, 'ro', markersize=8, label='Measured Performance')
        
        plt.xlabel('Load Factor (λ)', fontsize=12)
        plt.ylabel('Average Number of Probes', fontsize=12)
        plt.title('Successful Search Performance vs Load Factor', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('time_succ.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Plot for unsuccessful searches
        plt.figure(figsize=(12, 8))
        linear_fail = [0.5 * (1 + 1/((1-x)**2)) for x in lambda_vals]
        double_fail = [1/(1-x) for x in lambda_vals]
        measured_fail = [Q*x for x in results['unsuccessful']]
        
        plt.plot(lambda_vals, linear_fail, 'b-', linewidth=2, label='Linear Probing (Theory)')
        plt.plot(lambda_vals, double_fail, 'g-', linewidth=2, label='Double Hashing (Theory)')
        plt.plot(load_factors, measured_fail, 'ro', markersize=8, label='Measured Performance')
        
        plt.xlabel('Load Factor (λ)', fontsize=12)
        plt.ylabel('Average Number of Probes', fontsize=12)
        plt.title('Unsuccessful Search Performance vs Load Factor', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('time_fail.png', dpi=300, bbox_inches='tight')
        plt.close()