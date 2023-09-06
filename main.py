from flask import Flask, render_template, request, abort
from services.todos import TodoService
from drivers.sqlite_todos_driver import SqliteTodosDriver
from controller import TodoController

app = Flask(__name__)
todoService = TodoService(SqliteTodosDriver())
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


@app.route('/todos/toggle/:todo_id', methods=['PUT'])
def toggleTodo(todo_id):
    return controller.toggleTodo(todo_id)
