import os
from flask import Flask
from services.todos import TodoService
from drivers.sqlite_todos_driver import SqliteTodosDriver, close_db
from drivers.inmemory_todos_driver import InmemoryTodosDriver
from controller import TodoController

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.teardown_appcontext(close_db)
storageDriver = SqliteTodosDriver(os.path.join(basedir, 'db', 'todos.sqlite'))
# storageDriver = InmemoryTodosDriver()
todoService = TodoService(storageDriver)
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