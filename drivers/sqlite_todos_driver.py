import sqlite3
from models.todo import Todo
from flask import current_app, g

# https://flask.palletsprojects.com/en/2.3.x/tutorial/database/#connect-to-the-database
def get_db(filePath: str):
    if 'db' not in g:
        g.db = sqlite3.connect(filePath, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def init_db():
    db = get_db()

    with current_app.open_resource('./db/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

class SqliteTodosDriver:
    dbFilePath: str
    def __init__(self, dbFilePath: str) -> None:
        self.dbFilePath = dbFilePath

    def addTodo(self, todo: str) -> None:
        try:
            db = get_db(self.dbFilePath)
            db.execute(
                'INSERT INTO "todos" (todo, done) VALUES (?,?)', (todo, 0))
            db.commit()
        except:
            db.rollback()
            raise RuntimeError('Failed to write a todo to DB')
        finally:
            return None

    def toggleTodo(self, id: str) -> None:
        try:
            db = get_db(self.dbFilePath)
            todo = self.getById(id)
            newDone = int(not bool(todo.done))
            db.execute(
                'UPDATE "todos" SET "done"=? WHERE id=?', (newDone, todo.id))
            db.commit()
        except:
            db.rollback()
            raise RuntimeError('Failed to update the todo in DB')
        finally:
            return None

    def getAll(self) -> list[Todo]:
        try:
            db = get_db(self.dbFilePath)
            dbRows = db.execute('SELECT * FROM todos')
            result = []
            for row in dbRows:
                result.append(Todo(row['id'], row['todo'], bool(row['done'])))
            return result
        except:
            raise RuntimeError('Failed to read todos from DB')

    def getById(self, id) -> Todo:
        try:
            db = get_db(self.dbFilePath)
            cur = db.execute('SELECT * FROM "todos" WHERE "id" = ?', id)
            row = cur.fetchone()
            return Todo(row['id'], row['todo'], bool(row['done']))
        except:
            raise RuntimeError('Failed to read a todo from DB')
