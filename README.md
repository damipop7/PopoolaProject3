# Hash Table Analysis Project

## Environment
- Language: Python 3.8+
- IDE: Visual Studio Code
- Required packages: numpy, matplotlib

## Installation
```bash
pip install numpy matplotlib
```

## Project Structure
- `hash_table.py`: Main hash table implementation
- `data_generator.py`: Generates test data
- `timing_analysis.py`: Performance analysis code
- `visualizer.py`: Visualization utilities
- `test_hash_table.py`: Unit tests
- `main.py`: Main execution script

## Hashing
The hash table implements linear probing for collision resolution with two resize strategies:
1. Double the table size
2. Add 10000 to the table size

The table stores string values and uses Python's built-in hash() function for hashing.

## Running the Project
```bash
python main.py
```

For tests:
```bash
python -m unittest test_hash_table.py
```

## Conclusions

### A. Graph Analysis
The timing graphs show:
- Rehash timing reveals the cost of different resize strategies
- Load factor graphs demonstrate the theoretical vs actual performance
- The curves follow the expected mathematical models

### B. Hash Table Addition Time
- Double strategy: O(n) amortized time for insertions
- Add 10000 strategy: More frequent resizing but smaller individual costs

### C. Strategy Comparison
Double Strategy:
- Pros: Better amortized performance
- Cons: Large individual resize operations

Add 10000 Strategy:
- Pros: More predictable resize times
- Cons: More frequent resizing operations

### D. Optimal Load Factor
Based on the timing results, a load factor between 0.5 and 0.7 provides:
- Good balance between space usage and performance
- Acceptable search times for both successful and unsuccessful searches
- Reasonable resize frequency

### E. Linear Probe Performance
The measured results closely match the theoretical predictions:
- Successful searches follow the 1/2(1 + 1/(1-λ)) curve
- Unsuccessful searches follow the 1/2(1 + 1/(1-λ)²) curve

### F. Surprising Results
- The stability of performance up to λ = 0.7
- The sharp degradation after λ = 0.8
- The consistency between theoretical and actual results