from flask import Flask
from services.todos import TodoService
from drivers.sqlite_todos_driver import SqliteTodosDriver
from drivers.inmemory_todos_driver import InmemoryTodosDriver
from controller import TodoController

app = Flask(__name__)
todosDbDriver = SqliteTodosDriver()
inmemoryDriver = InmemoryTodosDriver()
# I feel like in-memory storage today
# ... at least until I figure out why am I having issues with the DB
todoService = TodoService(inmemoryDriver)
controller = TodoController(todoService)


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
