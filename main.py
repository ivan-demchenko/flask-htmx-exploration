from flask import Flask, render_template, request
from todosService import TodoService

app = Flask(__name__)
todoService = TodoService()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/todos')
def todos():
  return render_template('todos.html', todos=todoService.getAll())

@app.route('/add-todo', methods=['POST'])
def addTodo():
  todoName = request.form['todo-name']
  return render_template('todos.html', todos=todoService.addTodo(todoName))

@app.route('/toggle-todo/<int:todo_id>', methods=['PUT'])
def toggleTodo(todo_id: int):
  updatedTodos = todoService.toggleTodo(todo_id)
  return render_template('todos.html', todos=updatedTodos)