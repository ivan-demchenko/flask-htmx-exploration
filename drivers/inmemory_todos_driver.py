from models.todo import Todo


class InmemoryTodosDriver:
    todos: list[Todo] = []

    def addTodo(self, todo: str) -> None:
        self.todos.append(
            Todo(len(self.todos), todo, False)
        )

    def toggleTodo(self, id: str) -> None:
        todoIdx = int(id)
        self.todos[todoIdx].done = not self.todos[todoIdx].done

    def getAll(self) -> list[Todo]:
        return self.todos
