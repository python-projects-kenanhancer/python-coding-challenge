"""
Python Dataclasses Demo

This demo showcases various features of Python dataclasses including:
- Basic dataclass creation
- Default values and field defaults
- Type hints and validation
- Custom methods
- Inheritance
- Field metadata and post-init processing
- Comparison and ordering
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional
from datetime import datetime


# Basic dataclass example
@dataclass
class Person:
    """A simple person dataclass with basic fields."""
    name: str
    age: int
    email: str


# Dataclass with default values
@dataclass
class Employee:
    """Employee dataclass with default values and optional fields."""
    name: str
    employee_id: int
    department: str = "General"
    salary: float = 50000.0
    is_active: bool = True
    skills: List[str] = field(default_factory=list)
    hire_date: Optional[datetime] = None


# Dataclass with custom methods
@dataclass
class Product:
    """Product dataclass with custom methods and validation."""
    name: str
    price: float
    category: str
    in_stock: bool = True
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Post-initialization processing."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not self.name.strip():
            raise ValueError("Product name cannot be empty")
    
    def add_tag(self, tag: str) -> None:
        """Add a tag to the product."""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def get_discounted_price(self, discount_percent: float) -> float:
        """Calculate discounted price."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        return self.price * (1 - discount_percent / 100)
    
    def __str__(self) -> str:
        """Custom string representation."""
        return f"{self.name} (${self.price:.2f}) - {self.category}"


# Dataclass with ordering
@dataclass(order=True)
class Student:
    """Student dataclass with ordering capabilities."""
    name: str
    grade: float
    student_id: int
    
    def __post_init__(self):
        """Ensure grade is valid."""
        if not 0 <= self.grade <= 100:
            raise ValueError("Grade must be between 0 and 100")


# Dataclass with inheritance
@dataclass
class Vehicle:
    """Base vehicle dataclass."""
    make: str
    model: str
    year: int
    color: str = "White"
    
    def get_age(self) -> int:
        """Calculate vehicle age."""
        return datetime.now().year - self.year


@dataclass
class Car(Vehicle):
    """Car dataclass inheriting from Vehicle."""
    doors: int = 4
    fuel_type: str = "Gasoline"
    mileage: float = 0.0
    
    def get_fuel_efficiency(self) -> str:
        """Get fuel efficiency category based on fuel type."""
        if self.fuel_type.lower() == "electric":
            return "Excellent"
        elif self.fuel_type.lower() == "hybrid":
            return "Good"
        else:
            return "Average"


@dataclass
class Motorcycle:
    """Motorcycle dataclass with composition instead of inheritance."""
    make: str
    model: str
    year: int
    engine_size: float
    color: str = "White"
    has_sidecar: bool = False
    
    def get_age(self) -> int:
        """Calculate vehicle age."""
        return datetime.now().year - self.year
    
    def get_engine_category(self) -> str:
        """Categorize engine size."""
        if self.engine_size < 250:
            return "Small"
        elif self.engine_size < 500:
            return "Medium"
        else:
            return "Large"


def main():
    """Main function demonstrating dataclass usage."""
    print("=" * 60)
    print("PYTHON DATACLASSES DEMO")
    print("=" * 60)
    
    # Basic dataclass usage
    print("\n1. Basic Dataclass:")
    person = Person("Alice Johnson", 28, "alice@example.com")
    print(f"Person: {person}")
    print(f"Name: {person.name}, Age: {person.age}")
    
    # Dataclass with defaults
    print("\n2. Dataclass with Default Values:")
    employee1 = Employee("Bob Smith", 1001)
    employee2 = Employee("Carol Davis", 1002, "Engineering", 75000.0)
    
    print(f"Employee 1: {employee1}")
    print(f"Employee 2: {employee2}")
    
    # Adding skills
    employee1.skills.extend(["Python", "JavaScript"])
    employee2.skills.extend(["Java", "React", "Docker"])
    print(f"Employee 1 skills: {employee1.skills}")
    print(f"Employee 2 skills: {employee2.skills}")
    
    # Product with custom methods
    print("\n3. Product with Custom Methods:")
    product = Product("Laptop", 999.99, "Electronics")
    product.add_tag("portable")
    product.add_tag("work")
    product.add_tag("portable")  # Duplicate won't be added
    
    print(f"Product: {product}")
    print(f"Tags: {product.tags}")
    print(f"Discounted price (20% off): ${product.get_discounted_price(20):.2f}")
    
    # Error handling
    try:
        Product("", -50.0, "Invalid")
    except ValueError as e:
        print(f"Error creating product: {e}")
    
    # Student with ordering
    print("\n4. Student with Ordering:")
    students = [
        Student("David", 85.5, 2001),
        Student("Eve", 92.0, 2002),
        Student("Frank", 78.5, 2003),
        Student("Grace", 95.0, 2004)
    ]
    
    print("Students (unsorted):")
    for student in students:
        print(f"  {student}")
    
    print("\nStudents (sorted by grade):")
    for student in sorted(students, reverse=True):
        print(f"  {student}")
    
    # Vehicle inheritance
    print("\n5. Vehicle Inheritance:")
    car = Car("Toyota", "Camry", 2020, "Blue", 4, "Hybrid", 25000.0)
    motorcycle = Motorcycle("Honda", "CBR600", 2019, 600.0, "Red")
    
    print(f"Car: {car}")
    print(f"  Age: {car.get_age()} years")
    print(f"  Fuel efficiency: {car.get_fuel_efficiency()}")
    
    print(f"Motorcycle: {motorcycle}")
    print(f"  Age: {motorcycle.get_age()} years")
    print(f"  Engine category: {motorcycle.get_engine_category()}")
    
    # Dataclass utilities
    print("\n6. Dataclass Utilities:")
    print(f"Person as dict: {asdict(person)}")
    print(f"Person as tuple: {astuple(person)}")
    
    # Field metadata example
    @dataclass
    class Config:
        """Example with field metadata."""
        api_key: str = field(metadata={"description": "API key for authentication"})
        timeout: int = field(default=30, metadata={"description": "Request timeout in seconds"})
        retries: int = field(default=3, metadata={"description": "Number of retry attempts"})
    
    config = Config("secret-key-123")
    print(f"\nConfig: {config}")
    
    # Access field metadata
    import dataclasses
    for field_info in dataclasses.fields(config):
        print(f"  {field_info.name}: {field_info.metadata.get('description', 'No description')}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
