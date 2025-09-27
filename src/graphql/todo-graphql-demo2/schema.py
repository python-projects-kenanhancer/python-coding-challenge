import strawberry
from typing import List, Optional
from uuid import UUID, uuid4
from models import Todo, todos




@strawberry.type
class TodoType:
    id: UUID
    title: str
    description: str
    completed: bool


@strawberry.type
class Query:
    @strawberry.field
    def get_todos(self) -> List[TodoType]:
        return todos

    @strawberry.field
    def get_todo_by_id(self, id: UUID) -> Optional[TodoType]:
        return next((t for t in todos if t.id == id), None)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_todo(self, title: str, description: str) -> TodoType:
        todo = Todo(id=uuid4(), title=title, description=description)
        todos.append(todo)
        return todo

    @strawberry.mutation
    def toggle_todo(self, id: UUID) -> Optional[TodoType]:
        for todo in todos:
            if todo.id == id:
                todo.completed = not todo.completed
                return todo
        return None

    @strawberry.mutation
    def delete_todo(self, id: UUID) -> bool:
        global todos
        initial = len(todos)
        todos = [t for t in todos if t.id != id]
        return len(todos) < initial


schema = strawberry.Schema(query=Query, mutation=Mutation)
