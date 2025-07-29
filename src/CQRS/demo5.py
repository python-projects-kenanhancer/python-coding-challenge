# CQRS Python Example 5


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


# Command and Query base classes
class Command(Message):
    def __init__(self, content, user_id):
        super().__init__(content)
        self.user_id = user_id


class Query(Message):
    def __init__(self, content):
        super().__init__(content)
        self.read_only = True


# Event base class extending Message
class Event(Message):
    def __init__(self, event_type, content):
        super().__init__(content)
        self.event_type = event_type


# EventBus for handling event publication and processing
class EventBus:
    def __init__(self):
        self.event_queue = []

    def publish(self, event):
        print(f"Event Published: {event.event_type}")
        self.event_queue.append(event)

    def process_events(self, dispatcher):
        while self.event_queue:
            event = self.event_queue.pop(0)
            dispatcher.process_event(event)
            time.sleep(0.5)


# MessageBus for handling commands and queries
class MessageBus:
    def __init__(self):
        self.message_queue = []

    def send(self, message):
        print(f"Message sent to queue: {message}")
        self.message_queue.append(message)

    def process_messages(self, dispatcher):
        while self.message_queue:
            message = self.message_queue.pop(0)
            dispatcher.process_message(message)
            time.sleep(0.5)


# Dispatcher class as the central hub for registering handlers and dispatching messages
class Dispatcher:
    def __init__(self, message_bus, event_bus):
        self.message_bus = message_bus
        self.event_bus = event_bus
        self.command_handlers = {}
        self.query_handlers = {}
        self.event_handlers = {}

    def register_command_handler(self, command_type, handler):
        self.command_handlers[command_type] = handler

    def register_query_handler(self, query_type, handler):
        self.query_handlers[query_type] = handler

    def register_event_handler(self, event_type, handler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def dispatch(self, message):
        if isinstance(message, Command) or isinstance(message, Query):
            self.message_bus.send(message)
        elif isinstance(message, Event):
            self.event_bus.publish(message)
        else:
            print("Unknown message type")

    def process_message(self, message):
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

    def process_event(self, event):
        handlers = self.event_handlers.get(event.event_type, [])
        for handler in handlers:
            handler().handle(event)


# Command classes
class CreateOrderCommand(Command):
    def __init__(self, order_id, user_id, items):
        super().__init__({"order_id": order_id, "items": items}, user_id)
        self.order_id = order_id


class UpdateUserCommand(Command):
    def __init__(self, user_id, new_data):
        super().__init__({"new_data": new_data}, user_id)
        self.new_data = new_data


# Event classes
class OrderCreatedEvent(Event):
    def __init__(self, order_id, user_id, items):
        super().__init__(
            "OrderCreated", {"order_id": order_id, "user_id": user_id, "items": items}
        )


class UserUpdatedEvent(Event):
    def __init__(self, user_id, new_data):
        super().__init__("UserUpdated", {"user_id": user_id, "new_data": new_data})


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
        # Dispatch OrderCreated event after command execution
        dispatcher.dispatch(
            OrderCreatedEvent(
                command.order_id, command.user_id, command.content["items"]
            )
        )


class UpdateUserHandler:
    def handle(self, command):
        user_id = command.user_id
        if user_id in database.users:
            database.users[user_id].update(command.new_data)
            print(f"User {user_id} updated with data: {command.new_data}")
            # Dispatch UserUpdated event after successful update
            dispatcher.dispatch(UserUpdatedEvent(user_id, command.new_data))
        else:
            print(f"User {user_id} does not exist.")


# Query classes
class GetUserOrdersQuery(Query):
    def __init__(self, user_id):
        super().__init__({"user_id": user_id})
        self.user_id = user_id


class GetOrderDetailsQuery(Query):
    def __init__(self, order_id):
        super().__init__({"order_id": order_id})
        self.order_id = order_id


# Query handlers
class GetUserOrdersHandler:
    def handle(self, query):
        user_orders = [
            order
            for order in database.orders.values()
            if order["user_id"] == query.user_id
        ]
        print(f"Orders for user {query.user_id}: {user_orders}")


class GetOrderDetailsHandler:
    def handle(self, query):
        order = database.orders.get(query.order_id, None)
        print(f"Order details for order {query.order_id}: {order}")


# Event handlers
class OrderCreatedEventHandler:
    def handle(self, event):
        print(f"Handling OrderCreatedEvent for order ID: {event.content['order_id']}")


class UserUpdatedEventHandler:
    def handle(self, event):
        print(f"Handling UserUpdatedEvent for user ID: {event.content['user_id']}")


# Instantiate buses and dispatcher
message_bus = MessageBus()
event_bus = EventBus()
dispatcher = Dispatcher(message_bus, event_bus)

# Register handlers via Dispatcher
dispatcher.register_command_handler(CreateOrderCommand, CreateOrderHandler)
dispatcher.register_command_handler(UpdateUserCommand, UpdateUserHandler)
dispatcher.register_query_handler(GetUserOrdersQuery, GetUserOrdersHandler)
dispatcher.register_query_handler(GetOrderDetailsQuery, GetOrderDetailsHandler)
dispatcher.register_event_handler("OrderCreated", OrderCreatedEventHandler)
dispatcher.register_event_handler("UserUpdated", UserUpdatedEventHandler)

# Example usage
# Sending commands and queries to the Dispatcher
dispatcher.dispatch(CreateOrderCommand("1001", "u1", ["item1", "item2"]))
dispatcher.dispatch(
    UpdateUserCommand("u1", {"name": "Alice", "email": "alice@example.com"})
)
dispatcher.dispatch(GetUserOrdersQuery("u1"))
dispatcher.dispatch(GetOrderDetailsQuery("1001"))

# Process all messages and then process events
message_bus.process_messages(dispatcher)
event_bus.process_events(dispatcher)
