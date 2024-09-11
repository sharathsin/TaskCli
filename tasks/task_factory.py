from tasks.exceptions import InvalidTaskTypeException


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Task({self.title}, {self.description})"


class Bug(Task):
    def __init__(self, title, description, severity):
        super().__init__(title, description)
        self.severity = severity


class Feature(Task):
    def __init__(self, title, description, priority):
        super().__init__(title, description)
        self.priority = priority


class TaskFactory:
    @staticmethod
    def create_task(task_type, *args):
        if task_type == 'bug':
            return Bug(*args)
        elif task_type == 'feature':
            return Feature(*args)
        else:
            raise InvalidTaskTypeException(f"Task type {task_type} is not supported")
