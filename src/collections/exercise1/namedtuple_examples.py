"""
Python NamedTuple - Comprehensive Examples
==========================================

NamedTuple creates tuple subclasses with named fields. It provides the benefits
of tuples (immutable, hashable) with the readability of named attributes.
"""

from collections import namedtuple
import json
from typing import NamedTuple
from dataclasses import dataclass

# 1. Basic NamedTuple Creation
print("=== BASIC NAMEDTUPLE CREATION ===")

# Create a simple namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 1 x: {p1.x}, y: {p1.y}")
print(f"Point 2 x: {p2.x}, y: {p2.y}")

# Create with string field names
Person = namedtuple('Person', 'name age city')
person1 = Person('Alice', 25, 'New York')
person2 = Person(name='Bob', age=30, city='Boston')

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# 2. NamedTuple Methods and Properties
print("\n=== NAMEDTUPLE METHODS AND PROPERTIES ===")

# Access by index or name
print(f"Point 1[0]: {p1[0]}")  # Access by index
print(f"Point 1.x: {p1.x}")    # Access by name

# Get field names
print(f"Point fields: {Point._fields}")

# Create from iterable
p3 = Point._make([5, 6])
print(f"Point from _make: {p3}")

# Convert to dictionary
point_dict = p1._asdict()
print(f"Point as dict: {point_dict}")

# Replace fields (returns new instance)
p4 = p1._replace(x=10)
print(f"Original: {p1}")
print(f"Replaced: {p4}")

# 3. Advanced NamedTuple Creation
print("\n=== ADVANCED NAMEDTUPLE CREATION ===")

# NamedTuple with default values
def create_namedtuple_with_defaults(name, fields, defaults=None):
    """Create namedtuple with default values."""
    if defaults is None:
        defaults = {}
    
    # Create the base namedtuple
    nt = namedtuple(name, fields)
    
    # Create a new class with defaults
    class NamedTupleWithDefaults(nt):
        def __new__(cls, *args, **kwargs):
            # Fill in defaults for missing arguments
            full_kwargs = {}
            
            # Handle positional arguments
            for i, field in enumerate(fields):
                if i < len(args):
                    full_kwargs[field] = args[i]
                elif field in kwargs:
                    full_kwargs[field] = kwargs[field]
                elif field in defaults:
                    full_kwargs[field] = defaults[field]
                else:
                    raise TypeError(f"Missing required argument: {field}")
            
            # Handle keyword-only arguments
            for field in kwargs:
                if field not in fields:
                    raise TypeError(f"Unexpected keyword argument: {field}")
            
            return super().__new__(cls, **full_kwargs)
    
    return NamedTupleWithDefaults

# Create a namedtuple with defaults
Config = create_namedtuple_with_defaults(
    'Config', 
    ['host', 'port', 'timeout', 'debug'], 
    {'port': 8080, 'timeout': 30, 'debug': False}
)

config1 = Config('localhost')
config2 = Config('example.com', port=3000, debug=True)
print(f"Config 1: {config1}")
print(f"Config 2: {config2}")

# 4. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# 1. RGB Color
RGB = namedtuple('RGB', 'red green blue')
color1 = RGB(255, 128, 0)  # Orange
color2 = RGB(red=0, green=255, blue=128)  # Green

print(f"Color 1: {color1}")
print(f"Color 2: {color2}")

def color_to_hex(color):
    """Convert RGB color to hex."""
    return f"#{color.red:02x}{color.green:02x}{color.blue:02x}"

print(f"Color 1 hex: {color_to_hex(color1)}")
print(f"Color 2 hex: {color_to_hex(color2)}")

# 2. Student Record
Student = namedtuple('Student', 'name age grade subjects')
student1 = Student('Alice', 18, 'A', ['Math', 'Science', 'English'])
student2 = Student('Bob', 17, 'B', ['History', 'Art'])

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")

# 3. Employee Record
Employee = namedtuple('Employee', 'id name department salary')
employees = [
    Employee(1, 'John Doe', 'Engineering', 75000),
    Employee(2, 'Jane Smith', 'Marketing', 65000),
    Employee(3, 'Bob Johnson', 'Engineering', 80000),
    Employee(4, 'Alice Brown', 'HR', 60000)
]

print("Employees:")
for emp in employees:
    print(f"  {emp.name}: {emp.department}, ${emp.salary:,}")

# 5. NamedTuple with Methods
print("\n=== NAMEDTUPLE WITH METHODS ===")

class Point(namedtuple('Point', 'x y')):
    """Point namedtuple with methods."""
    
    def distance_from_origin(self):
        """Calculate distance from origin."""
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to(self, other):
        """Calculate distance to another point."""
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
    
    def __add__(self, other):
        """Add two points."""
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Multiply point by scalar."""
        return Point(self.x * scalar, self.y * scalar)

# Test Point methods
p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance from origin: {p1.distance_from_origin()}")
print(f"Distance between points: {p1.distance_to(p2)}")
print(f"Point addition: {p1 + p2}")
print(f"Point multiplication: {p1 * 2}")

# 6. NamedTuple for Database Records
print("\n=== NAMEDTUPLE FOR DATABASE RECORDS ===")

# Simulate database records
Order = namedtuple('Order', 'id customer_id product quantity price date')
orders = [
    Order(1, 101, 'Laptop', 1, 999.99, '2024-01-15'),
    Order(2, 102, 'Mouse', 2, 29.99, '2024-01-16'),
    Order(3, 101, 'Keyboard', 1, 79.99, '2024-01-17'),
    Order(4, 103, 'Monitor', 1, 299.99, '2024-01-18'),
    Order(5, 102, 'Laptop', 1, 999.99, '2024-01-19')
]

# Calculate total revenue
total_revenue = sum(order.quantity * order.price for order in orders)
print(f"Total revenue: ${total_revenue:.2f}")

# Group orders by customer
customer_orders = {}
for order in orders:
    if order.customer_id not in customer_orders:
        customer_orders[order.customer_id] = []
    customer_orders[order.customer_id].append(order)

print("Orders by customer:")
for customer_id, customer_orders_list in customer_orders.items():
    customer_total = sum(order.quantity * order.price for order in customer_orders_list)
    print(f"  Customer {customer_id}: {len(customer_orders_list)} orders, Total: ${customer_total:.2f}")

# 7. NamedTuple for API Responses
print("\n=== NAMEDTUPLE FOR API RESPONSES ===")

# API response structure
ApiResponse = namedtuple('ApiResponse', 'status_code data message timestamp')

def create_api_response(status_code, data=None, message="", timestamp=None):
    """Create API response."""
    if timestamp is None:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
    return ApiResponse(status_code, data, message, timestamp)

# Simulate API responses
success_response = create_api_response(200, {"user_id": 123, "name": "Alice"}, "User retrieved successfully")
error_response = create_api_response(404, None, "User not found")

print(f"Success response: {success_response}")
print(f"Error response: {error_response}")

# 8. NamedTuple vs Regular Classes
print("\n=== NAMEDTUPLE VS REGULAR CLASSES ===")

# Regular class
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"RegularPoint(x={self.x}, y={self.y})"

# NamedTuple class
NamedPoint = namedtuple('NamedPoint', 'x y')

# Performance comparison
import time

def time_point_creation(n_points):
    """Time point creation."""
    # Regular class
    start_time = time.time()
    regular_points = [RegularPoint(i, i*2) for i in range(n_points)]
    regular_time = time.time() - start_time
    
    # NamedTuple
    start_time = time.time()
    named_points = [NamedPoint(i, i*2) for i in range(n_points)]
    named_time = time.time() - start_time
    
    return regular_time, named_time

regular_time, named_time = time_point_creation(100000)
print(f"Regular class creation time: {regular_time:.6f}s")
print(f"NamedTuple creation time: {named_time:.6f}s")
print(f"NamedTuple is {regular_time/named_time:.1f}x faster")

# 9. NamedTuple for Configuration
print("\n=== NAMEDTUPLE FOR CONFIGURATION ===")

# Database configuration
DatabaseConfig = namedtuple('DatabaseConfig', 
                          'host port username password database_name ssl_enabled')

# Application configuration
AppConfig = namedtuple('AppConfig', 
                      'debug log_level database_config api_key')

# Create configurations
db_config = DatabaseConfig(
    host='localhost',
    port=5432,
    username='admin',
    password='secret',
    database_name='myapp',
    ssl_enabled=True
)

app_config = AppConfig(
    debug=True,
    log_level='INFO',
    database_config=db_config,
    api_key='abc123'
)

print(f"Database config: {db_config}")
print(f"App config: {app_config}")
print(f"DB host: {app_config.database_config.host}")

# 10. NamedTuple with Validation
print("\n=== NAMEDTUPLE WITH VALIDATION ===")

class ValidatedPerson(namedtuple('ValidatedPerson', 'name age email')):
    """Person namedtuple with validation."""
    
    def __new__(cls, name, age, email):
        # Validate name
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        
        # Validate age
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("Age must be an integer between 0 and 150")
        
        # Validate email (simple check)
        if '@' not in email:
            raise ValueError("Email must contain @")
        
        return super().__new__(cls, name, age, email)

# Test validation
try:
    valid_person = ValidatedPerson("Alice", 25, "alice@example.com")
    print(f"Valid person: {valid_person}")
except ValueError as e:
    print(f"Validation error: {e}")

try:
    invalid_person = ValidatedPerson("", -5, "invalid-email")
    print(f"Invalid person: {invalid_person}")
except ValueError as e:
    print(f"Validation error: {e}")

# 11. NamedTuple Serialization
print("\n=== NAMEDTUPLE SERIALIZATION ===")

# Convert to dictionary for JSON serialization
person_dict = person1._asdict()
print(f"Person as dict: {person_dict}")

# JSON serialization
person_json = json.dumps(person_dict)
print(f"Person as JSON: {person_json}")

# Deserialize from JSON
person_from_json = json.loads(person_json)
person_restored = Person(**person_from_json)
print(f"Person restored from JSON: {person_restored}")

# 12. NamedTuple with Inheritance
print("\n=== NAMEDTUPLE WITH INHERITANCE ===")

# Base namedtuple
BaseShape = namedtuple('BaseShape', 'name area')

class Shape(BaseShape):
    """Shape with additional methods."""
    
    def is_large(self):
        """Check if shape is large."""
        return self.area > 100
    
    def describe(self):
        """Describe the shape."""
        size = "large" if self.is_large() else "small"
        return f"{self.name} is a {size} shape with area {self.area}"

# Create shapes
shapes = [
    Shape("Circle", 78.5),
    Shape("Square", 144),
    Shape("Triangle", 45.2)
]

print("Shapes:")
for shape in shapes:
    print(f"  {shape.describe()}")

# 13. NamedTuple for Game Development
print("\n=== NAMEDTUPLE FOR GAME DEVELOPMENT ===")

# Game entities
Position = namedtuple('Position', 'x y z')
Player = namedtuple('Player', 'id name position health level')
Item = namedtuple('Item', 'id name type value weight')

# Create game objects
player = Player(
    id=1,
    name="Hero",
    position=Position(10, 5, 0),
    health=100,
    level=5
)

sword = Item(
    id=101,
    name="Iron Sword",
    type="weapon",
    value=50,
    weight=3.5
)

potion = Item(
    id=102,
    name="Health Potion",
    type="consumable",
    value=10,
    weight=0.5
)

print(f"Player: {player}")
print(f"Sword: {sword}")
print(f"Potion: {potion}")

# 14. NamedTuple vs TypedDict vs Dataclass
print("\n=== NAMEDTUPLE VS TYPEDDICT VS DATACLASS ===")

from typing import TypedDict

# TypedDict
class PersonTypedDict(TypedDict):
    name: str
    age: int
    city: str

# Dataclass
@dataclass
class PersonDataclass:
    name: str
    age: int
    city: str

# NamedTuple
PersonNamedTuple = namedtuple('PersonNamedTuple', 'name age city')

# Create instances
typed_dict_person = PersonTypedDict(name="Alice", age=25, city="NYC")
dataclass_person = PersonDataclass(name="Bob", age=30, city="Boston")
namedtuple_person = PersonNamedTuple(name="Charlie", age=35, city="Chicago")

print(f"TypedDict: {typed_dict_person}")
print(f"Dataclass: {dataclass_person}")
print(f"NamedTuple: {namedtuple_person}")

# Comparison
print(f"TypedDict is mutable: {not hasattr(typed_dict_person, '_fields')}")
print(f"Dataclass is mutable: {not hasattr(dataclass_person, '_fields')}")
print(f"NamedTuple is immutable: {hasattr(namedtuple_person, '_fields')}")

# 15. NamedTuple Factory Functions
print("\n=== NAMEDTUPLE FACTORY FUNCTIONS ===")

def create_geometry_factory():
    """Create geometry namedtuple factory."""
    Point = namedtuple('Point', 'x y')
    Line = namedtuple('Line', 'start end')
    Circle = namedtuple('Circle', 'center radius')
    
    return Point, Line, Circle

# Use factory
Point, Line, Circle = create_geometry_factory()

point = Point(0, 0)
line = Line(Point(0, 0), Point(5, 5))
circle = Circle(Point(2, 2), 3)

print(f"Point: {point}")
print(f"Line: {line}")
print(f"Circle: {circle}")

print("\n" + "="*50)
print("NamedTuple examples completed!")
print("="*50)
