from typing import List
from uuid import UUID
from dataclasses import dataclass


@dataclass
class Todo:
    id: UUID
    title: str
    description: str
    completed: bool = False


todos: List[Todo] = []
