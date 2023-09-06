from models.todo import Todo
from drivers.sqlite_todos_driver import SqliteTodosDriver


class TodoService:
    driver: SqliteTodosDriver | None = None

    def __init__(self, driver: SqliteTodosDriver) -> None:
        self.driver = driver

    def addTodo(self, todo: str) -> None:
        return self.driver.addTodo(todo)

    def toggleTodo(self, id: str) -> None:
        return self.driver.toggleTodo(id)

    def getAll(self) -> list[Todo]:
        return self.driver.getAll()
