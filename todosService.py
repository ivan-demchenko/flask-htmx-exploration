class Todo:
  todo: str
  done: bool

  def __init__(self, todo, done):
    self.todo = todo
    self.done = done

class TodoService:
  todos: list

  def __init__(self) -> None:
    self.todos = []

  def addTodo(self, todo: str) -> list:
    if (todo == ''):
      return self.todos
    else:
      self.todos.append(Todo(todo, False))
      return self.todos

  def toggleTodo(self, index: int):
    self.todos[index].done = not self.todos[index].done;
    return self.todos

  def getAll(self) -> list:
    return self.todos