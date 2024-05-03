from task import Task
from taskmanager import TaskManager

def main():

    taskMan = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Remove Task")
        print("3. Display Task")
        print("4. Assign Priority")
        print("5. Filter Tasks by Priority")
        print("6. Mark Task as Complete")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            taskMan.createTask(description, priority)
        
        elif choice == '2':
            description = input("Enter task description to remove: ")
            taskMan.removeTask(description)
        
        elif choice == '3':
            taskMan.displayTasks()
        
        elif choice == '4':
            description = input("Enter task description to assign priority: ")
            priority = input("Enter new priority (High, Medium, Low): ")
            taskMan.assignPriority(description, priority)
        
        elif choice == '5':
            description = input("Enter priority to filter tasks (High, Medium, Low): ")
            taskMan.filterByPriority(priority)
        
        elif choice == '6':
            description = input("Enter task description to mark as complete: ")
            taskMan.markComplete(description)

        elif choice == '7':
            print("Exiting Task Manager.")
            break
        
        else:
            print("Invalid choice, please try again")
        
if __name__ == "__main__":
    main()