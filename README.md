# Package Sorting Robot

A Python implementation of a robotic arm package sorting system for Thoughtful's automation factory.

## Problem Statement

The robotic arm must sort packages into three categories based on their dimensions and mass:

- **STANDARD**: Packages that are neither bulky nor heavy
- **SPECIAL**: Packages that are either bulky or heavy (but not both)
- **REJECTED**: Packages that are both bulky and heavy

### Sorting Criteria

- **Bulky**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg

## Files

- `package_sorter.py` - Main sorting function
- `test_package_sorter.py` - Comprehensive test suite
- `demo.py` - Example usage and demonstration
- `README.md` - This file

## Usage

### Basic Usage

```python
from package_sorter import sort

result = sort(width, height, length, mass)
print(result)  # Returns "STANDARD", "SPECIAL", or "REJECTED"
```

### Examples

```python
sort(50, 50, 50, 10)    # Returns "STANDARD"
sort(150, 50, 50, 10)   # Returns "SPECIAL" (bulky)
sort(50, 50, 50, 20)    # Returns "SPECIAL" (heavy)
sort(150, 50, 50, 20)   # Returns "REJECTED" (both bulky and heavy)
```

## Running the Code

### Run Tests

```bash
python test_package_sorter.py
```

### Run Demo

```bash
python demo.py
```

### Run Both

```bash
python test_package_sorter.py && python demo.py
```

## Test Coverage

The test suite covers:

- Standard packages (under all limits)
- Bulky packages (volume or dimension limits exceeded)
- Heavy packages (mass limit exceeded)
- Rejected packages (both bulky and heavy)
- Edge cases (exactly at limits)

## Implementation Details

The `sort()` function:

1. Calculates package volume (width × height × length)
2. Determines if package is bulky (volume ≥ 1M cm³ OR any dimension ≥ 150 cm)
3. Determines if package is heavy (mass ≥ 20 kg)
4. Returns appropriate stack category based on conditions

## Time Complexity

- **Time**: O(1) - Constant time operations
- **Space**: O(1) - Constant space usage

## Edge Cases Handled

- Packages exactly at dimension limits (150 cm)
- Packages exactly at mass limit (20 kg)
- Packages exactly at volume limit (1,000,000 cm³)
- Various combinations of bulky and heavy conditions
