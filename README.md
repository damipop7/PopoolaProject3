# PopoolaProject3

## Hash Table Implementation Project

## Development Environment
- **Language**: Python 3.11
- **IDE**: Visual Studio Code
- **Required Packages**: pytest (for running tests)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/damipop7/PopoolaProject3.git
cd PopoolaProject3
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install pytest
```

## Project Structure
```
PopoolaProject3/
├── hash_table.py     # Hash table implementation
├── test_hash_table.py # Test cases
├── .gitignore
└── README.md
```

## Hashing
This project implements a custom hash table that stores string values directly (without key-value pairs). The implementation includes:

- **Hash Function**: Uses Python's built-in `hash()` function modded by table size
- **Collision Resolution**: Linear probing
- **Dynamic Resizing**: Two strategies:
  1. Double the size
  2. Add 10000 to the size
- **Load Factor**: Triggers resize when (count + 1) / size >= specified load factor

### Key Features
- Insert strings with collision handling
- Find strings with boolean return
- Dynamic resizing based on load factor
- Two resize strategies

### Test Cases
The implementation includes test cases verifying:
1. Basic insertion and finding of 5 strings
2. Resize behavior with 23 values (single resize)
3. Resize behavior with 24 values (double resize)
4. Both resize strategies (doubling and adding 10000)