# Python Collections - Comprehensive Examples

This directory contains comprehensive examples for all Python collection data types, designed to help you practice and understand each collection type thoroughly.

## Collection Types Covered

### 1. **Lists** (`list_examples.py`)
- Basic list creation and operations
- Adding and removing elements
- List comprehensions
- Performance considerations
- Common pitfalls and best practices
- Practical examples (student grades, shopping lists)

### 2. **Tuples** (`tuple_examples.py`)
- Basic tuple creation and operations
- Tuple unpacking and methods
- Immutable nature and performance
- Named tuples introduction
- Practical examples (coordinates, RGB colors)
- Comparison with lists

### 3. **Sets** (`set_examples.py`)
- Basic set creation and operations
- Set operations (union, intersection, difference)
- Set comprehensions
- Frozen sets
- Practical examples (tag systems, permission systems)
- Performance comparisons

### 4. **Dictionaries** (`dict_examples.py`)
- Basic dictionary creation and operations
- Dictionary methods and views
- Dictionary comprehensions
- Nested dictionaries
- Performance and best practices
- Practical examples (phone books, configuration)

### 5. **Counter** (`counter_examples.py`)
- Basic Counter creation and operations
- Counter methods and arithmetic operations
- Practical examples (text analysis, voting, dice simulation)
- Performance comparisons
- Advanced use cases

### 6. **Deque** (`deque_examples.py`)
- Basic deque creation and operations
- Deque methods and maxlen
- Practical examples (LRU cache, BFS, task scheduling)
- Performance comparisons with lists
- Advanced algorithms

### 7. **NamedTuple** (`namedtuple_examples.py`)
- Basic NamedTuple creation
- NamedTuple methods and properties
- Practical examples (RGB colors, student records)
- Comparison with regular classes
- Advanced features and validation

### 8. **OrderedDict** (`ordereddict_examples.py`)
- Basic OrderedDict creation and operations
- OrderedDict methods
- Comparison with regular dicts
- Practical examples (LRU cache, configuration management)
- Performance considerations

### 9. **ChainMap** (`chainmap_examples.py`)
- Basic ChainMap creation and operations
- ChainMap methods and properties
- Practical examples (configuration management, scope simulation)
- Performance comparisons
- Best practices

## How to Use These Examples

1. **Start with the basics**: Begin with `list_examples.py` to understand fundamental concepts
2. **Run the examples**: Each file is designed to be run independently
3. **Experiment**: Modify the examples to see how different operations work
4. **Practice**: Try implementing similar examples with your own data
5. **Compare**: Notice the differences between collection types and their use cases

## Key Learning Points

### When to Use Each Collection:

- **Lists**: When you need ordered, mutable sequences with potential duplicates
- **Tuples**: When you need ordered, immutable sequences (coordinates, records)
- **Sets**: When you need unique elements and set operations
- **Dictionaries**: When you need key-value mappings with fast lookups
- **Counter**: When you need to count occurrences of elements
- **Deque**: When you need efficient operations at both ends (queues, stacks)
- **NamedTuple**: When you need tuple benefits with named fields
- **OrderedDict**: When you need dictionary with guaranteed order (pre-Python 3.7)
- **ChainMap**: When you need to combine multiple mappings with priority

### Performance Characteristics:

- **Lists**: O(1) append, O(n) insert/delete at arbitrary positions
- **Tuples**: O(1) access, immutable
- **Sets**: O(1) average case for add/remove/lookup
- **Dictionaries**: O(1) average case for get/set/delete
- **Deque**: O(1) operations at both ends
- **Counter**: Similar to dict performance
- **NamedTuple**: Similar to tuple performance
- **OrderedDict**: Slightly slower than dict due to ordering
- **ChainMap**: O(k) lookup where k is number of mappings

## Running the Examples

```bash
# Run individual examples
python list_examples.py
python tuple_examples.py
python set_examples.py
python dict_examples.py
python counter_examples.py
python deque_examples.py
python namedtuple_examples.py
python ordereddict_examples.py
python chainmap_examples.py

# Or run all examples
for file in *.py; do
    echo "Running $file"
    python "$file"
    echo "---"
done
```

## Additional Resources

- [Python Collections Documentation](https://docs.python.org/3/library/collections.html)
- [Python Data Structures Tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python Collections Guide](https://realpython.com/python-collections/)

## Tips for Practice

1. **Start simple**: Begin with basic operations before moving to complex examples
2. **Experiment**: Try modifying the examples to see different outcomes
3. **Time operations**: Use the performance examples to understand efficiency
4. **Combine collections**: Try using multiple collection types together
5. **Solve problems**: Use these collections to solve real-world problems
6. **Read the output**: Each example includes detailed explanations and output

Happy coding and practicing with Python collections!
