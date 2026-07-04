from data import tasks
from models import Task


def add_task():

    title = input("Enter task: ").strip()

    if title == "":
        print("Task cannot be empty.")
        return

    task = Task(len(tasks) + 1, title)

    tasks.append(task.to_dict())

    print("Task added successfully.")


def view_tasks():

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks\n")

    for task in tasks:
        print(f"{task['id']}. {task['title']}")


def delete_task():

    if len(tasks) == 0:
        print("Nothing to delete.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to delete: "))

        found = False

        for task in tasks:
            if task["id"] == number:
                tasks.remove(task)
                found = True
                break

        if found:

            for index, task in enumerate(tasks):
                task["id"] = index + 1

            print("Task deleted.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def search_task():

    keyword = input("Search: ").lower()

    found = False

    for task in tasks:

        if keyword in task["title"].lower():
            print(f"{task['id']}. {task['title']}")
            found = True

    if not found:
        print("No matching task found.")