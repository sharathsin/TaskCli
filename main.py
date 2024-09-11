from tasks.task_manager import TaskManager


def get_task_details(task_type):
    title = input(f"Enter {task_type} title: ")
    description = input(f"Enter {task_type} description: ")
    return title, description


def handle_add_bug(manager):
    title, description = get_task_details('bug')
    severity = input("Enter bug severity: ")
    manager.add_task('bug', title, description, severity)


def handle_add_feature(manager):
    title, description = get_task_details('feature')
    priority = input("Enter feature priority: ")
    manager.add_task('feature', title, description, priority)


def handle_task_addition(manager):
    task_type = input("Enter task type (bug/feature): ").lower()
    if task_type == 'bug':
        handle_add_bug(manager)
    elif task_type == 'feature':
        handle_add_feature(manager)
    else:
        print("Invalid task type. Please enter 'bug' or 'feature'.")


def handle_task_removal(manager):
    """Handles task removal."""
    title = input("Enter task title to remove: ")
    if not manager.remove_task(title):
        print(f"Task with title '{title}' not found.")


def show_menu(manager):
    """Display the menu and process user choices."""
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_task_addition(manager)
        elif choice == "2":
            handle_task_removal(manager)
        elif choice == "3":
            manager.list_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    manager = TaskManager()
    show_menu(manager)
