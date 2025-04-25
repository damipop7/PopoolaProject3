from timing_analysis import TimingAnalysis
from visualizer import Visualizer
import numpy as np

def calculate_Q_factor(load_factors, results):
    """Calculate scaling factor Q"""
    # Use load factor of 0.5 as reference point
    ref_idx = np.argmin(abs(load_factors - 0.5))
    measured = results['successful'][ref_idx]
    theoretical = 0.5 * (1 + 1/(1-0.5))
    return theoretical / measured

def main(test_mode=False):
    # Initialize timing analysis
    print("Initializing timing analysis...")
    timer = TimingAnalysis()
    
    if test_mode:
        print("Running in test mode with reduced dataset...")
        q_values = list(range(4, 8))  # Convert to list for length checking
        test_size = sum((3/4) * (2**q) - 1 for q in q_values)
        print(f"Will process approximately {int(test_size)} values across {len(q_values)} q-values")
    else:
        print("Running full analysis (this may take several minutes)...")
        q_values = list(range(4, 18))
    
    # Run rehash timing analysis
    print("\nStarting rehash timing analysis...")
    rehash_results = timer.time_rehash_strategies(q_values)
    
    if not rehash_results['no_rehash']:  # Check if results are empty
        print("Error: No results generated from timing analysis")
        return
    
    # Run load factor timing analysis
    print("\nStarting load factor timing analysis...")
    load_factors, load_results = timer.time_load_factors()
    
    if not load_results['successful']:  # Check if results are empty
        print("Error: No results generated from load factor analysis")
        return
    
    # Calculate Q factor from results
    Q = calculate_Q_factor(load_factors, load_results)
    print(f"\nCalculated Q factor: {Q:.2e}")
    
    # Create visualizations
    print("\nGenerating plots...")
    viz = Visualizer()
    viz.plot_rehash_timing(q_values, rehash_results)
    viz.plot_load_factor_timing(load_factors, load_results, Q=Q)
    print("Analysis complete!")

if __name__ == "__main__":
    try:
        main(test_mode=True)
    except Exception as e:
        print(f"Error during execution: {str(e)}")