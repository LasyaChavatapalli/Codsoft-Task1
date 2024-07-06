# Define an empty list to store tasks
tasklist = []

# Function to display the to-do list
def display_tasks():
    if not tasklist:
        print("Your To-Do List is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasklist, start=1):
            if task["done"]:
                status = "Completed"
            else:
                status="Not Completed"
            print(f"{i}. {task['task']} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
    task = {"task": task_name, "done": False}
    tasklist.append(task)
    print(f"Task '{task_name}' added to your To-Do List.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Create task")
    print("3. Update task")
    print("4. Remove task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        x=input("Enter the task: ")
        add_task(x)
    elif choice == '3':
        display_tasks()
        task_num = int(input("Enter the task number5 to update as completed: "))
        if 1 <= task_num <= len(tasklist):
            tasklist[task_num - 1]["done"] = True
            print(f"Task {task_num} updated as completed.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        display_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasklist):
            tasklist.pop(task_num - 1)
            print(f"Task {task_num} removed from your To-Do List.")
        else:
            print("Invalid task number.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")