# CQRS Python Example 1


import time
from datetime import datetime
import uuid


# In-memory database
class Database:
    def __init__(self):
        self.users = {}
        self.orders = {}


database = Database()


# Base class for all messages
class Message:
    def __init__(self, content):
        self.content = content
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.now()


# Command base class extending Message
class Command(Message):
    def __init__(self, content, user_id):
        super().__init__(content)
        self.user_id = user_id


# Query base class extending Message
class Query(Message):
    def __init__(self, content):
        super().__init__(content)
        self.read_only = True


# Command classes
class CreateOrderCommand(Command):
    def __init__(self, order_id, user_id, items):
        super().__init__({"order_id": order_id, "items": items}, user_id)
        self.order_id = order_id


class UpdateUserCommand(Command):
    def __init__(self, user_id, new_data):
        super().__init__({"new_data": new_data}, user_id)
        self.new_data = new_data


# Query classes
class GetUserOrdersQuery(Query):
    def __init__(self, user_id):
        super().__init__({"user_id": user_id})
        self.user_id = user_id


class GetOrderDetailsQuery(Query):
    def __init__(self, order_id):
        super().__init__({"order_id": order_id})
        self.order_id = order_id


# Command handlers
class CreateOrderHandler:
    def handle(self, command):
        order = {
            "order_id": command.order_id,
            "user_id": command.user_id,
            "items": command.content["items"],
        }
        database.orders[command.order_id] = order
        print(f"Order Created: {order}")


class UpdateUserHandler:
    def handle(self, command):
        user_id = command.user_id
        if user_id in database.users:
            database.users[user_id].update(command.new_data)
            print(f"User {user_id} updated with data: {command.new_data}")
        else:
            print(f"User {user_id} does not exist.")


# Query handlers
class GetUserOrdersHandler:
    def handle(self, query):
        user_id = query.user_id
        user_orders = [
            order for order in database.orders.values() if order["user_id"] == user_id
        ]
        print(f"Orders for user {user_id}: {user_orders}")
        return user_orders


class GetOrderDetailsHandler:
    def handle(self, query):
        order_id = query.order_id
        order = database.orders.get(order_id, None)
        print(f"Order details for order {order_id}: {order}")
        return order


# Dispatcher implementing the Open-Closed Principle
class Dispatcher:
    def __init__(self):
        # Handler registry for commands and queries
        self.command_handlers = {}
        self.query_handlers = {}

    def register_command_handler(self, command_type, handler):
        self.command_handlers[command_type] = handler

    def register_query_handler(self, query_type, handler):
        self.query_handlers[query_type] = handler

    def dispatch(self, message):
        if isinstance(message, Command):
            handler = self.command_handlers.get(type(message))
            if handler:
                handler().handle(message)
            else:
                print(f"No handler registered for command: {type(message)}")
        elif isinstance(message, Query):
            handler = self.query_handlers.get(type(message))
            if handler:
                handler().handle(message)
            else:
                print(f"No handler registered for query: {type(message)}")
        else:
            print("Unknown message type")


# Function to simulate sending a message to the queue
def send_message(message):
    message_queue.append(message)
    print(f"Message sent: {message}")


# Message Queue to simulate asynchronous processing
message_queue = []


# Simulated message processing loop
def process_messages():
    dispatcher = Dispatcher()
    # Register command and query handlers
    dispatcher.register_command_handler(CreateOrderCommand, CreateOrderHandler)
    dispatcher.register_command_handler(UpdateUserCommand, UpdateUserHandler)
    dispatcher.register_query_handler(GetUserOrdersQuery, GetUserOrdersHandler)
    dispatcher.register_query_handler(GetOrderDetailsQuery, GetOrderDetailsHandler)

    while message_queue:
        message = message_queue.pop(0)  # Get the first message from the queue
        dispatcher.dispatch(message)
        time.sleep(0.5)  # Simulate processing time


# Sending commands and queries to the queue
send_message(CreateOrderCommand("1001", "u1", ["item1", "item2"]))
send_message(UpdateUserCommand("u1", {"name": "Alice", "email": "alice@example.com"}))
send_message(GetUserOrdersQuery("u1"))
send_message(GetOrderDetailsQuery("1001"))

# Process all messages in the queue
process_messages()
