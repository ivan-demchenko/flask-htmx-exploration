from flask import render_template, request, abort
from services.todos import TodoService


class TodoController:
    todoService: TodoService | None = None

    def __init__(self, service: TodoService) -> None:
        self.todoService = service

    def index(self):
        return render_template('index.html')

    def getTodos(self):
        return render_template('todos.html', todos=self.todoService.getAll())

    def addTodo(self):
        todoName = request.form['todo-name']
        try:
            if (todoName == ''):
                return render_template('todos.html', todos=self.todoService.getAll())
            else:
                self.todoService.addTodo(todoName)
                return render_template('todos.html', todos=self.todoService.getAll())
        except:
            abort(500)

    def toggleTodo(self, todo_id):
        try:
            self.todoService.toggleTodo(todo_id)
            return render_template('todos.html', todos=self.todoService.getAll())
        except:
            abort(500)
