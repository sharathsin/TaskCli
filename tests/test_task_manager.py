import pytest
from tasks.task_manager import TaskManager
from tasks.exceptions import TaskNotFoundException


def test_add_and_find_task():
    manager = TaskManager()
    manager.add_task('bug', 'Fix Login', 'Critical login bug', 'High')
    task = manager.find_task('Fix Login')
    assert task.title == 'Fix Login'


def test_remove_task():
    manager = TaskManager()
    manager.add_task('feature', 'Dark Mode', 'Add dark mode to UI', 'High')
    manager.remove_task('Dark Mode')
    with pytest.raises(TaskNotFoundException):
        manager.find_task('Dark Mode')


def test_invalid_task_type():
    manager = TaskManager()
    with pytest.raises(Exception):
        manager.add_task('invalid', 'Task 1', 'Invalid task')


if __name__ == "__main__":
    pytest.main()
