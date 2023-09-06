class Todo:
    id: int
    todo: str
    done: bool

    def __init__(self, id: int, todo: str, done: bool):
        self.id = id
        self.todo = todo
        self.done = done
