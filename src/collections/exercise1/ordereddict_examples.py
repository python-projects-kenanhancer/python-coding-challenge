"""
Python OrderedDict - Comprehensive Examples
===========================================

OrderedDict is a dictionary subclass that remembers the order in which
items were inserted. Since Python 3.7, regular dicts also maintain insertion
order, but OrderedDict provides additional methods and guarantees.
"""

from collections import OrderedDict
import json

# 1. Basic OrderedDict Creation and Operations
print("=== BASIC ORDEREDDICT OPERATIONS ===")

# Creating OrderedDict
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print(f"OrderedDict: {od}")

# Create from regular dict (Python 3.7+ maintains order, but OrderedDict is explicit)
regular_dict = {'a': 1, 'b': 2, 'c': 3}
od_from_dict = OrderedDict(regular_dict)
print(f"From regular dict: {od_from_dict}")

# Create from list of tuples
od_from_list = OrderedDict([('x', 10), ('y', 20), ('z', 30)])
print(f"From list of tuples: {od_from_list}")

# Create with keyword arguments
od_kwargs = OrderedDict(first=1, second=2, third=3)
print(f"From kwargs: {od_kwargs}")

# 2. OrderedDict Methods
print("\n=== ORDEREDDICT METHODS ===")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"Initial OrderedDict: {od}")

# move_to_end() - moves key to end
od.move_to_end('a')
print(f"After move_to_end('a'): {od}")

# move_to_end() with last=False - moves key to beginning
od.move_to_end('d', last=False)
print(f"After move_to_end('d', last=False): {od}")

# popitem() - removes and returns last item
last_item = od.popitem()
print(f"Popped last item: {last_item}")
print(f"After popitem(): {od}")

# popitem(last=False) - removes and returns first item
first_item = od.popitem(last=False)
print(f"Popped first item: {first_item}")
print(f"After popitem(last=False): {od}")

# 3. OrderedDict vs Regular Dict
print("\n=== ORDEREDDICT VS REGULAR DICT ===")

# In Python 3.7+, regular dicts maintain insertion order
regular_dict = {}
regular_dict['first'] = 1
regular_dict['second'] = 2
regular_dict['third'] = 3

ordered_dict = OrderedDict()
ordered_dict['first'] = 1
ordered_dict['second'] = 2
ordered_dict['third'] = 3

print(f"Regular dict: {regular_dict}")
print(f"OrderedDict: {ordered_dict}")
print(f"Are they equal? {regular_dict == ordered_dict}")

# Key difference: OrderedDict has additional methods
print(f"OrderedDict methods: {[m for m in dir(ordered_dict) if not m.startswith('_')]}")

# 4. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# 1. LRU Cache Implementation
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """Get value and mark as recently used."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        """Put value and mark as recently used."""
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
            
            self.cache[key] = value
        
        print(f"Cache after put({key}, {value}): {dict(self.cache)}")

# Test LRU Cache
cache = LRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.get(1)  # Access 1
cache.put(4, "D")  # Should remove 2 (least recently used)

# 2. Configuration Management
print("\n=== CONFIGURATION MANAGEMENT ===")

class ConfigManager:
    def __init__(self):
        self.config = OrderedDict()
        self.load_defaults()
    
    def load_defaults(self):
        """Load default configuration."""
        defaults = [
            ('debug', False),
            ('port', 8080),
            ('host', 'localhost'),
            ('timeout', 30),
            ('max_connections', 100)
        ]
        
        for key, value in defaults:
            self.config[key] = value
    
    def update_config(self, updates):
        """Update configuration with new values."""
        for key, value in updates.items():
            if key in self.config:
                # Move to end to indicate it was recently modified
                self.config.move_to_end(key)
            self.config[key] = value
    
    def get_recently_modified(self, n=3):
        """Get recently modified configuration keys."""
        return list(self.config.keys())[-n:]

# Test configuration manager
config_manager = ConfigManager()
print(f"Initial config: {dict(config_manager.config)}")

config_manager.update_config({'port': 3000, 'debug': True, 'api_key': 'secret123'})
print(f"After updates: {dict(config_manager.config)}")
print(f"Recently modified: {config_manager.get_recently_modified()}")

# 3. Task Queue with Priority
print("\n=== TASK QUEUE WITH PRIORITY ===")

class TaskQueue:
    def __init__(self):
        self.tasks = OrderedDict()
    
    def add_task(self, task_id, task_data, priority='normal'):
        """Add task with priority."""
        # Create task with metadata
        task = {
            'data': task_data,
            'priority': priority,
            'timestamp': __import__('time').time()
        }
        
        # If task already exists, move to end (update priority)
        if task_id in self.tasks:
            self.tasks.move_to_end(task_id)
        
        self.tasks[task_id] = task
        print(f"Added task {task_id}: {task_data}")
    
    def get_next_task(self):
        """Get next task (FIFO order)."""
        if not self.tasks:
            return None
        
        task_id, task = self.tasks.popitem(last=False)
        print(f"Processing task {task_id}: {task['data']}")
        return task_id, task
    
    def get_high_priority_tasks(self):
        """Get all high priority tasks."""
        high_priority = [(tid, task) for tid, task in self.tasks.items() 
                        if task['priority'] == 'high']
        return high_priority

# Test task queue
queue = TaskQueue()
queue.add_task('task1', 'Process payment', 'high')
queue.add_task('task2', 'Send email', 'normal')
queue.add_task('task3', 'Generate report', 'low')
queue.add_task('task4', 'Critical system check', 'high')

print(f"High priority tasks: {queue.get_high_priority_tasks()}")

print("Processing tasks:")
while queue.tasks:
    queue.get_next_task()

# 5. OrderedDict for Data Processing
print("\n=== ORDEREDDICT FOR DATA PROCESSING ===")

# Process data in order
data_pipeline = OrderedDict([
    ('validate', lambda x: x > 0),
    ('transform', lambda x: x * 2),
    ('filter', lambda x: x < 100),
    ('format', lambda x: f"Value: {x}")
])

def process_data(data, pipeline):
    """Process data through pipeline steps."""
    result = data
    steps_taken = []
    
    for step_name, step_func in pipeline.items():
        try:
            if step_name == 'validate' and not step_func(result):
                raise ValueError(f"Validation failed for {result}")
            elif step_name == 'filter' and not step_func(result):
                raise ValueError(f"Filter failed for {result}")
            elif step_name in ['transform', 'format']:
                result = step_func(result)
            
            steps_taken.append(step_name)
            print(f"  {step_name}: {result}")
        except ValueError as e:
            print(f"  {step_name} failed: {e}")
            break
    
    return result, steps_taken

# Test data processing
test_data = [5, 15, 25, 35, 45]
for data in test_data:
    print(f"Processing {data}:")
    result, steps = process_data(data, data_pipeline)
    print(f"  Result: {result}, Steps: {steps}")
    print()

# 6. OrderedDict for API Response Caching
print("\n=== ORDEREDDICT FOR API RESPONSE CACHING ===")

class APICache:
    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.hit_count = 0
        self.miss_count = 0
    
    def get(self, key):
        """Get cached response."""
        if key in self.cache:
            # Move to end (most recently used)
            response = self.cache[key]
            self.cache.move_to_end(key)
            self.hit_count += 1
            print(f"Cache HIT for {key}")
            return response
        else:
            self.miss_count += 1
            print(f"Cache MISS for {key}")
            return None
    
    def put(self, key, response):
        """Cache API response."""
        if key in self.cache:
            # Update existing
            self.cache[key] = response
            self.cache.move_to_end(key)
        else:
            # Add new
            if len(self.cache) >= self.max_size:
                # Remove least recently used
                self.cache.popitem(last=False)
            
            self.cache[key] = response
        
        print(f"Cached response for {key}")
    
    def get_stats(self):
        """Get cache statistics."""
        total = self.hit_count + self.miss_count
        hit_rate = (self.hit_count / total * 100) if total > 0 else 0
        return {
            'hit_count': self.hit_count,
            'miss_count': self.miss_count,
            'hit_rate': hit_rate,
            'cache_size': len(self.cache)
        }

# Test API cache
api_cache = APICache(max_size=3)

# Simulate API calls
responses = [
    ('user/123', {'name': 'Alice', 'id': 123}),
    ('user/456', {'name': 'Bob', 'id': 456}),
    ('user/789', {'name': 'Charlie', 'id': 789}),
    ('user/123', {'name': 'Alice', 'id': 123}),  # Should hit cache
    ('user/999', {'name': 'David', 'id': 999}),  # Should evict user/456
    ('user/456', {'name': 'Bob', 'id': 456}),   # Should miss cache
]

for endpoint, response in responses:
    cached_response = api_cache.get(endpoint)
    if cached_response is None:
        api_cache.put(endpoint, response)

print(f"Cache stats: {api_cache.get_stats()}")

# 7. OrderedDict for Configuration Hierarchies
print("\n=== ORDEREDDICT FOR CONFIGURATION HIERARCHIES ===")

class HierarchicalConfig:
    def __init__(self):
        self.configs = OrderedDict()
        self.load_order = []
    
    def add_config(self, name, config_dict, priority=0):
        """Add configuration with priority."""
        self.configs[name] = {
            'config': config_dict,
            'priority': priority
        }
        # Sort by priority (lower number = higher priority)
        self.load_order = sorted(self.configs.keys(), 
                               key=lambda k: self.configs[k]['priority'])
    
    def get_value(self, key):
        """Get value from highest priority config."""
        for config_name in self.load_order:
            config = self.configs[config_name]['config']
            if key in config:
                return config[key]
        return None
    
    def get_all_values(self, key):
        """Get all values for a key from all configs."""
        values = []
        for config_name in self.load_order:
            config = self.configs[config_name]['config']
            if key in config:
                values.append((config_name, config[key]))
        return values

# Test hierarchical config
hier_config = HierarchicalConfig()

# Add configs in different order
hier_config.add_config('default', {'debug': False, 'port': 8080, 'timeout': 30}, priority=100)
hier_config.add_config('environment', {'debug': True, 'port': 3000}, priority=50)
hier_config.add_config('user', {'timeout': 60, 'api_key': 'user123'}, priority=10)

print("Configuration hierarchy:")
for name in hier_config.load_order:
    config = hier_config.configs[name]
    print(f"  {name} (priority {config['priority']}): {config['config']}")

print(f"\nFinal values:")
print(f"  debug: {hier_config.get_value('debug')}")
print(f"  port: {hier_config.get_value('port')}")
print(f"  timeout: {hier_config.get_value('timeout')}")
print(f"  api_key: {hier_config.get_value('api_key')}")

print(f"\nAll timeout values: {hier_config.get_all_values('timeout')}")

# 8. OrderedDict for Workflow Management
print("\n=== ORDEREDDICT FOR WORKFLOW MANAGEMENT ===")

class Workflow:
    def __init__(self, name):
        self.name = name
        self.steps = OrderedDict()
        self.current_step = None
    
    def add_step(self, step_name, step_func, dependencies=None):
        """Add workflow step."""
        self.steps[step_name] = {
            'function': step_func,
            'dependencies': dependencies or [],
            'status': 'pending',
            'result': None
        }
    
    def execute_step(self, step_name):
        """Execute a specific step."""
        if step_name not in self.steps:
            raise ValueError(f"Step {step_name} not found")
        
        step = self.steps[step_name]
        
        # Check dependencies
        for dep in step['dependencies']:
            if self.steps[dep]['status'] != 'completed':
                raise ValueError(f"Dependency {dep} not completed")
        
        # Execute step
        try:
            step['status'] = 'running'
            result = step['function']()
            step['result'] = result
            step['status'] = 'completed'
            print(f"Step {step_name} completed: {result}")
        except Exception as e:
            step['status'] = 'failed'
            print(f"Step {step_name} failed: {e}")
    
    def execute_all(self):
        """Execute all steps in order."""
        for step_name in self.steps:
            if self.steps[step_name]['status'] == 'pending':
                self.execute_step(step_name)

# Test workflow
def step1():
    return "Data validated"

def step2():
    return "Data processed"

def step3():
    return "Report generated"

workflow = Workflow("Data Processing")
workflow.add_step('validate', step1)
workflow.add_step('process', step2, dependencies=['validate'])
workflow.add_step('report', step3, dependencies=['process'])

print("Executing workflow:")
workflow.execute_all()

# 9. OrderedDict Performance
print("\n=== ORDEREDDICT PERFORMANCE ===")

import time

def benchmark_dict_operations(n_operations=10000):
    """Benchmark dict vs OrderedDict operations."""
    
    # Regular dict
    regular_dict = {}
    start_time = time.time()
    for i in range(n_operations):
        regular_dict[i] = i
        if i % 1000 == 0:
            regular_dict.get(i - 500, None)  # Some lookups
    regular_time = time.time() - start_time
    
    # OrderedDict
    ordered_dict = OrderedDict()
    start_time = time.time()
    for i in range(n_operations):
        ordered_dict[i] = i
        if i % 1000 == 0:
            ordered_dict.get(i - 500, None)  # Some lookups
    ordered_time = time.time() - start_time
    
    return regular_time, ordered_time

regular_time, ordered_time = benchmark_dict_operations(10000)
print(f"Regular dict time: {regular_time:.6f}s")
print(f"OrderedDict time: {ordered_time:.6f}s")
print(f"OrderedDict overhead: {(ordered_time/regular_time - 1) * 100:.1f}%")

# 10. OrderedDict Serialization
print("\n=== ORDEREDDICT SERIALIZATION ===")

# OrderedDict maintains order in JSON serialization
ordered_data = OrderedDict([
    ('name', 'Alice'),
    ('age', 25),
    ('city', 'New York'),
    ('occupation', 'Engineer')
])

json_string = json.dumps(ordered_data, indent=2)
print(f"JSON with order preserved:\n{json_string}")

# Deserialize back to OrderedDict
import json
def json_to_ordereddict(data):
    """Convert JSON back to OrderedDict."""
    if isinstance(data, dict):
        return OrderedDict(data)
    elif isinstance(data, list):
        return [json_to_ordereddict(item) for item in data]
    else:
        return data

parsed_data = json.loads(json_string)
ordered_parsed = json_to_ordereddict(parsed_data)
print(f"Parsed back to OrderedDict: {ordered_parsed}")

print("\n" + "="*50)
print("OrderedDict examples completed!")
print("="*50)
