from timing_analysis import TimingAnalysis
from visualizer import Visualizer

def main():
    # Initialize timing analysis
    timer = TimingAnalysis()
    
    # Run rehash timing analysis
    q_values = range(4, 18)
    rehash_results = timer.time_rehash_strategies(q_values)  # This matches the method name now
    
    # Run load factor timing analysis
    load_factors, load_results = timer.time_load_factors()
    
    # Create visualizations
    viz = Visualizer()
    viz.plot_rehash_timing(q_values, rehash_results)
    
    # Calculate Q factor (scaling factor)
    Q = 1e-6  # This should be adjusted based on your actual timing results
    viz.plot_load_factor_timing(load_factors, load_results, Q)

if __name__ == "__main__":
    main()