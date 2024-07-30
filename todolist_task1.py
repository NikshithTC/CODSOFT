tasks = []

def add_task(task_description):
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'task': task_description,
        'status': 'Pending'
    }
    tasks.append(task)
    print(f"Task '{task_description}' added.")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = new_description
            print(f"Task {task_id} updated.")
            break
    else:
        print(f"Task {task_id} not found.")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Complete'
            print(f"Task {task_id} marked as complete.")
            break
    else:
        print(f"Task {task_id} not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        print(f"{task['id']}. {task['task']} - {task['status']}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            list_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
