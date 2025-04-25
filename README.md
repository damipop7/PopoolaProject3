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
- Rehash timing shows exponential growth with table size
- Load factor performance degrades as λ approaches 1
- Linear probing matches theoretical predictions

### B. Hash Table Addition Time
- Double strategy: O(n) amortized cost
- Add 10000 strategy: More frequent but smaller resizes

### C. Strategy Comparison
Double Strategy:
- Pros: Better amortized performance
- Cons: Large individual resize operations

Add 10000 Strategy:
- Pros: Predictable resize operations
- Cons: More frequent resizing needed

### D. Optimal Load Factor
Based on measurements, λ ≈ 0.7 provides:
- Good space utilization
- Reasonable search times
- Acceptable resize frequency

### E. Linear Probe Performance
Measured results closely match theoretical formulas:
- Successful searches: 1/2(1 + 1/(1-λ))
- Unsuccessful searches: 1/2(1 + 1/(1-λ)²)

### F. Surprising Results
- Performance stability up to λ = 0.7
- Sharp degradation after λ = 0.8
- Close match to theoretical predictions