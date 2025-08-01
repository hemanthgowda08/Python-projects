tasks = []

def show_menu():
    print("\n📌 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n🗂 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {status} {task['title']} [{task['category']}] (Priority: {task['priority']})")

def add_task():
    title = input("Enter task title: ")
    category = input("Enter category (e.g., Work, Personal, Study): ")
    priority = input("Enter priority (High/Medium/Low): ")
    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added.")

def edit_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to edit: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            task["title"] = input("New title: ") or task["title"]
            task["category"] = input("New category: ") or task["category"]
            task["priority"] = input("New priority: ") or task["priority"]
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()