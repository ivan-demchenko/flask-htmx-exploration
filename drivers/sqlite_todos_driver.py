import sqlite3
from models.todo import Todo


class SqliteTodosDriver:
    db = None

    def __init__(self):
        self.db = sqlite3.connect("./db/todos.db")
        self.db.execute(
            """CREATE TABLE IF NOT EXISTS "todos" (
              "id" INTEGER PRIMARY KEY AUTOINCREMENT,
              "todo" TEXT,
              "done" BOOLEAN NOT NULL CHECK ("done" IN (0, 1))
            )"""
        )

    def dispose(self):
        self.db.close()

    def addTodo(self, todo: str) -> None:
        try:
            self.db.execute(
                'INSERT INTO "todos" (todo, done) VALUES (?,?)', (todo, 0))
            self.db.commit()
        except:
            self.db.rollback()
            raise RuntimeError('Failed to write a todo to DB')
        finally:
            return None

    def toggleTodo(self, id: str) -> None:
        try:
            todo = self.getById(id)
            self.db.execute(
                'UPDATE "todos" SET "done"=? WHERE id=?', (int(todo.done), todo.id))
            self.db.commit()
        except:
            self.db.rollback()
            raise RuntimeError('Failed to update the todo in DB')
        finally:
            return None

    def getAll(self) -> list[Todo]:
        try:
            dbRows = self.db.execute('SELECT * FROM todos')
            result = []
            for row in dbRows:
                result.append(Todo(row.id, row.todo, bool(row.done)))
            return result
        except:
            raise RuntimeError('Failed to read todos from DB')

    def getById(self, id) -> Todo:
        try:
            cur = self.db.execute('SELECT * FROM "todos" WHERE "id" = ?', id)
            head = cur.fetchall()[0]
            return Todo(head.id, head.todo, bool(head.done))
        except:
            raise RuntimeError('Failed to read a todo from DB')
