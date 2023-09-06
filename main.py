import signal
import atexit
import sys
from flask import Flask
from services.todos import TodoService
from drivers.sqlite_todos_driver import SqliteTodosDriver
from drivers.inmemory_todos_driver import InmemoryTodosDriver
from controller import TodoController

app = Flask(__name__)
# storageDriver = SqliteTodosDriver("./db/todos.sqlite")

# Learn how make threads to share the db connection
storageDriver = InmemoryTodosDriver()
todoService = TodoService(storageDriver)
controller = TodoController(todoService)


def exit_handler():
    print("Cleaning up")
    storageDriver.dispose()


def kill_handler(*args):
    storageDriver.dispose()
    sys.exit(0)


atexit.register(exit_handler)
signal.signal(signal.SIGINT, kill_handler)
signal.signal(signal.SIGTERM, kill_handler)


@app.route('/')
def index():
    return controller.index()


@app.route('/todos')
def todos():
    return controller.getTodos()


@app.route('/todos', methods=['POST'])
def addTodo():
    return controller.addTodo()


@app.route('/todos/toggle/<todo_id>', methods=['PUT'])
def toggleTodo(todo_id):
    return controller.toggleTodo(todo_id)
