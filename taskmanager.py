from task import Task

class TaskManager:
    
    def __init__(self):
        self.tasks = []
    
    def createTask(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
    
    def removeTask(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
    
    def displayTasks(self):
        for task in self.tasks:
            print(f"{task.description} - Priority: {task.priority} - Completed: {task.completed}")

    def createTask(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
    
    def removeTask(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
    
    def displayTasks(self):
        for task in self.tasks:
            print(f"{task.description} - Priority: {task.priority} - Completed: {task.completed}")

    def assignPriority(self, description, priority):
        for task in self.tasks:
            if task.description == description:
                task.priority = priority

    def markComplete(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                self.removeTask(description)

    def filterByPriority(self, priority):
        filteredTasks = [task for task in self.tasks if task.priority == priority]
        for task in filteredTasks:
            print(f"{task.description} - Priority: {task.priority} - Completed {task.completed}")
                    