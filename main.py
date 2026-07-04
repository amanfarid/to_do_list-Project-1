import os

tasks = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def display_tasks():
    print("\n========== YOUR TASKS ==========\n")

    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{task['id']}. {task['title']}")


while True:

    clear_screen()

    print("=" * 40)
    print("         TO-DO LIST MANAGER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # Add Task
    if choice == "1":

        clear_screen()

        print("========== ADD TASK ==========\n")

        title = input("Enter task: ").strip()

        if title == "":
            print("\nTask cannot be empty.")

        else:
            task = {
                "id": len(tasks) + 1,
                "title": title
            }

            tasks.append(task)

            clear_screen()

            print("Task added successfully!\n")
            display_tasks()

        pause()

    # View Tasks
    elif choice == "2":

        clear_screen()

        display_tasks()

        pause()

    # Delete Task
    elif choice == "3":

        clear_screen()

        if not tasks:
            print("No tasks to delete.")
            pause()
            continue

        display_tasks()

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

                clear_screen()

                print("Task deleted successfully!\n")
                display_tasks()

            else:
                print("\nInvalid task number.")

        except ValueError:
            print("\nPlease enter a valid number.")

        pause()

    # Search Task
    elif choice == "4":

        clear_screen()

        keyword = input("Enter keyword to search: ").strip().lower()

        clear_screen()

        print("========== SEARCH RESULTS ==========\n")

        found = False

        for task in tasks:
            if keyword in task["title"].lower():
                print(f"{task['id']}. {task['title']}")
                found = True

        if not found:
            print("No matching task found.")

        pause()

    # Exit
    elif choice == "5":

        clear_screen()

        print("Thank you for using the To-Do List Manager.")
        break

    else:
        print("\nInvalid choice.")
        pause()