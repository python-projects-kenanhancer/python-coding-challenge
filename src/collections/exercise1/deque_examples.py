"""
Python Deque (Double-Ended Queue) - Comprehensive Examples
=========================================================

Deque is a double-ended queue that allows efficient addition and removal
of elements from both ends. It's part of the collections module.
"""

from collections import deque
import time
import random

# 1. Basic Deque Creation and Operations
print("=== BASIC DEQUE OPERATIONS ===")

# Creating deques
empty_deque = deque()
deque_from_list = deque([1, 2, 3, 4, 5])
deque_from_string = deque("hello")
deque_with_maxlen = deque([1, 2, 3], maxlen=5)

print(f"Empty deque: {empty_deque}")
print(f"From list: {deque_from_list}")
print(f"From string: {deque_from_string}")
print(f"With maxlen: {deque_with_maxlen}")
print(f"Maxlen: {deque_with_maxlen.maxlen}")

# 2. Adding Elements
print("\n=== ADDING ELEMENTS ===")

d = deque([1, 2, 3])
print(f"Initial deque: {d}")

# append() - adds to right end
d.append(4)
print(f"After append(4): {d}")

# appendleft() - adds to left end
d.appendleft(0)
print(f"After appendleft(0): {d}")

# extend() - adds multiple elements to right end
d.extend([5, 6, 7])
print(f"After extend([5, 6, 7]): {d}")

# extendleft() - adds multiple elements to left end (note: reverses order)
d.extendleft([-1, -2])
print(f"After extendleft([-1, -2]): {d}")

# insert() - inserts at specific position
d.insert(3, 99)
print(f"After insert(3, 99): {d}")

# 3. Removing Elements
print("\n=== REMOVING ELEMENTS ===")

d = deque([1, 2, 3, 4, 5, 6, 7])
print(f"Initial deque: {d}")

# pop() - removes from right end
popped_right = d.pop()
print(f"Popped from right: {popped_right}")
print(f"After pop(): {d}")

# popleft() - removes from left end
popped_left = d.popleft()
print(f"Popped from left: {popped_left}")
print(f"After popleft(): {d}")

# remove() - removes first occurrence
d.remove(4)
print(f"After remove(4): {d}")

# clear() - removes all elements
d.clear()
print(f"After clear(): {d}")

# 4. Deque with maxlen
print("\n=== DEQUE WITH MAXLEN ===")

# Create deque with maximum length
d = deque(maxlen=3)
print(f"Empty deque with maxlen=3: {d}")

# Add elements
d.append(1)
d.append(2)
d.append(3)
print(f"After adding 1, 2, 3: {d}")

# Adding more elements will remove from the opposite end
d.append(4)
print(f"After append(4): {d}")

d.appendleft(0)
print(f"After appendleft(0): {d}")

d.extend([5, 6])
print(f"After extend([5, 6]): {d}")

# 5. Accessing and Modifying Elements
print("\n=== ACCESSING AND MODIFYING ELEMENTS ===")

d = deque([10, 20, 30, 40, 50])
print(f"Deque: {d}")

# Indexing
print(f"First element: {d[0]}")
print(f"Last element: {d[-1]}")
print(f"Middle element: {d[2]}")

# Slicing
print(f"First 3 elements: {list(d)[:3]}")
print(f"Last 3 elements: {list(d)[-3:]}")

# Modifying elements
d[1] = 25
print(f"After modifying index 1: {d}")

# 6. Rotating Elements
print("\n=== ROTATING ELEMENTS ===")

d = deque([1, 2, 3, 4, 5])
print(f"Initial deque: {d}")

# rotate() - positive rotates right
d.rotate(2)
print(f"After rotate(2): {d}")

# rotate() - negative rotates left
d.rotate(-1)
print(f"After rotate(-1): {d}")

# rotate() with maxlen
d = deque([1, 2, 3], maxlen=3)
print(f"Deque with maxlen: {d}")
d.rotate(1)
print(f"After rotate(1): {d}")

# 7. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# 1. Sliding Window
def sliding_window_max(nums, k):
    """Find maximum in each sliding window of size k."""
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices of elements smaller than current
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_window = sliding_window_max(nums, k)
print(f"Array: {nums}")
print(f"Sliding window max (k={k}): {max_window}")

# 2. Undo/Redo System
class UndoRedoSystem:
    def __init__(self, max_history=10):
        self.history = deque(maxlen=max_history)
        self.current_state = 0
    
    def save_state(self, state):
        """Save a state for undo/redo."""
        # Remove any states after current if we're in middle of history
        while len(self.history) > self.current_state + 1:
            self.history.pop()
        
        self.history.append(state)
        self.current_state = len(self.history) - 1
        print(f"Saved state: {state}")
    
    def undo(self):
        """Undo to previous state."""
        if self.current_state > 0:
            self.current_state -= 1
            print(f"Undo to: {self.history[self.current_state]}")
            return self.history[self.current_state]
        else:
            print("Nothing to undo")
            return None
    
    def redo(self):
        """Redo to next state."""
        if self.current_state < len(self.history) - 1:
            self.current_state += 1
            print(f"Redo to: {self.history[self.current_state]}")
            return self.history[self.current_state]
        else:
            print("Nothing to redo")
            return None

# Test undo/redo system
undo_system = UndoRedoSystem(max_history=5)
undo_system.save_state("Initial state")
undo_system.save_state("After edit 1")
undo_system.save_state("After edit 2")
undo_system.save_state("After edit 3")

undo_system.undo()
undo_system.undo()
undo_system.redo()
undo_system.redo()

# 8. Deque for BFS (Breadth-First Search)
print("\n=== DEQUE FOR BFS ===")

# Simple graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    """Breadth-first search using deque."""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

bfs_result = bfs(graph, 'A')
print(f"BFS traversal from A: {bfs_result}")

# 9. Deque for Task Scheduling
print("\n=== DEQUE FOR TASK SCHEDULING ===")

class TaskScheduler:
    def __init__(self):
        self.high_priority = deque()
        self.normal_priority = deque()
        self.low_priority = deque()
    
    def add_task(self, task, priority="normal"):
        """Add task with specified priority."""
        if priority == "high":
            self.high_priority.append(task)
        elif priority == "low":
            self.low_priority.append(task)
        else:
            self.normal_priority.append(task)
        print(f"Added {priority} priority task: {task}")
    
    def get_next_task(self):
        """Get next task (high -> normal -> low priority)."""
        if self.high_priority:
            return self.high_priority.popleft()
        elif self.normal_priority:
            return self.normal_priority.popleft()
        elif self.low_priority:
            return self.low_priority.popleft()
        else:
            return None
    
    def has_tasks(self):
        """Check if there are any tasks."""
        return bool(self.high_priority or self.normal_priority or self.low_priority)

# Test task scheduler
scheduler = TaskScheduler()
scheduler.add_task("Send email", "high")
scheduler.add_task("Update documentation", "low")
scheduler.add_task("Code review", "normal")
scheduler.add_task("Fix critical bug", "high")
scheduler.add_task("Organize files", "low")

print("Processing tasks:")
while scheduler.has_tasks():
    task = scheduler.get_next_task()
    print(f"  Processing: {task}")

# 10. Deque for LRU Cache Implementation
print("\n=== DEQUE FOR LRU CACHE ===")

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_order = deque()
    
    def get(self, key):
        """Get value and update access order."""
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        """Put value and update access order."""
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                lru_key = self.access_order.popleft()
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.access_order.append(key)
        
        print(f"Cache after put({key}, {value}): {dict(self.cache)}")

# Test LRU cache
cache = LRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.get(1)  # Access 1
cache.put(4, "D")  # Should remove 2 (least recently used)

# 11. Performance Comparison
print("\n=== PERFORMANCE COMPARISON ===")

# Compare list vs deque for queue operations
def test_queue_performance(n_operations=10000):
    # Test with list
    start_time = time.time()
    lst = []
    for i in range(n_operations):
        lst.append(i)  # O(1)
        if lst:
            lst.pop(0)  # O(n) - inefficient for large lists
    list_time = time.time() - start_time
    
    # Test with deque
    start_time = time.time()
    dq = deque()
    for i in range(n_operations):
        dq.append(i)  # O(1)
        if dq:
            dq.popleft()  # O(1) - efficient
    deque_time = time.time() - start_time
    
    print(f"List operations time: {list_time:.6f}s")
    print(f"Deque operations time: {deque_time:.6f}s")
    print(f"Deque is {list_time/deque_time:.1f}x faster")

test_queue_performance()

# 12. Deque for Palindrome Check
print("\n=== DEQUE FOR PALINDROME CHECK ===")

def is_palindrome(text):
    """Check if text is palindrome using deque."""
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    dq = deque(cleaned)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

test_strings = ["racecar", "A man a plan a canal Panama", "hello", "Madam", "12321"]
for text in test_strings:
    result = is_palindrome(text)
    print(f"'{text}' is palindrome: {result}")

# 13. Deque for Expression Evaluation
print("\n=== DEQUE FOR EXPRESSION EVALUATION ===")

def evaluate_postfix(expression):
    """Evaluate postfix expression using deque as stack."""
    stack = deque()
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            # Pop two operands
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            else:
                raise ValueError(f"Unknown operator: {token}")
            
            stack.append(result)
    
    return stack.pop()

expressions = ["3 4 +", "5 1 2 + 4 * +", "15 7 1 1 + - / 3 *"]
for expr in expressions:
    result = evaluate_postfix(expr)
    print(f"'{expr}' = {result}")

# 14. Deque for Moving Average
print("\n=== DEQUE FOR MOVING AVERAGE ===")

class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
    
    def add(self, value):
        """Add new value and return current average."""
        self.window.append(value)
        return sum(self.window) / len(self.window)
    
    def get_average(self):
        """Get current average."""
        return sum(self.window) / len(self.window) if self.window else 0

# Test moving average
ma = MovingAverage(3)
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Moving average (window=3):")
for value in values:
    avg = ma.add(value)
    print(f"  Add {value}, average: {avg:.2f}")

# 15. Deque for Round Robin Scheduling
print("\n=== DEQUE FOR ROUND ROBIN SCHEDULING ===")

class RoundRobinScheduler:
    def __init__(self, time_quantum=2):
        self.ready_queue = deque()
        self.time_quantum = time_quantum
    
    def add_process(self, process_id, burst_time):
        """Add process to ready queue."""
        self.ready_queue.append((process_id, burst_time))
        print(f"Added process {process_id} with burst time {burst_time}")
    
    def schedule(self):
        """Execute round robin scheduling."""
        print("Round Robin Scheduling:")
        current_time = 0
        
        while self.ready_queue:
            process_id, remaining_time = self.ready_queue.popleft()
            
            if remaining_time <= self.time_quantum:
                # Process completes
                current_time += remaining_time
                print(f"  Time {current_time}: Process {process_id} completed")
            else:
                # Process needs more time
                current_time += self.time_quantum
                remaining_time -= self.time_quantum
                self.ready_queue.append((process_id, remaining_time))
                print(f"  Time {current_time}: Process {process_id} executed, remaining time: {remaining_time}")

# Test round robin scheduling
scheduler = RoundRobinScheduler(time_quantum=2)
scheduler.add_process("P1", 5)
scheduler.add_process("P2", 3)
scheduler.add_process("P3", 1)
scheduler.add_process("P4", 4)
scheduler.schedule()

print("\n" + "="*50)
print("Deque examples completed!")
print("="*50)
