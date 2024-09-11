from tasks.task_factory import TaskFactory
from tasks.exceptions import TaskNotFoundException


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_type, *args):
        task = TaskFactory.create_task(task_type, *args)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            print(f"Task removed: {task}")

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        raise TaskNotFoundException(f"Task with title '{title}' not found")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)
