import unittest
from taskmanager import TaskManager
from task import Task

class TestTask(unittest.TestCase):
    
    def setUp(self):
        self.taskMan = TaskManager()

    def test_TaskCreation(self):
        task = Task("Test", "High")
        self.assertEqual(task.description, "Test")
        self.assertEqual(task.priority, "High")
        self.assertFalse(task.completed)

    def test_CreateTask(self):
        self.taskMan.createTask("Test", "High")
        self.assertEqual(len(self.taskMan.tasks), 1)
    
    def test_RemoveTask(self):
        self.taskMan.createTask("Test", "High")
        self.taskMan.removeTask("Test")
        self.assertEqual(len(self.taskMan.tasks), 0)
    
    def test_MarkComplete(self):
        self.taskMan.createTask("Test", "High")
        self.taskMan.markComplete("Test")
        self.assertEqual(len(self.taskMan.tasks), 1)
    
    def test_AssignPriority(self):
        self.taskMan.createTask("Test", "High")
        self.taskMan.assignPriority("Test", "Low")
        self.assertEqual(self.taskMan.tasks[0].priority, "Low")

    def test_FilterByPriority(self):
        self.taskMan.createTask("Task 1", "High")
        self.taskMan.createTask("Task 2", "Low")
        self.taskMan.createTask("Task 3", "Medium")
        self.taskMan.filterByPriority("High")
        self.assertEqual(len(self.taskMan.tasks), 3)
        self.assertEqual(self.taskMan.tasks[0].description, "Task 1")

    def test_AssignPriorityMarkComplete(self):
        self.taskMan.createTask("Test", "High")
        self.taskMan.assignPriority("Test", "Low")
        self.taskMan.markComplete("Test")
        self.assertEqual(len(self.taskMan.tasks), 1)
        self.assertTrue(self.taskMan.tasks[0].completed)
        self.assertEqual(self.taskMan.tasks[0].priority, "Low")
    
    def test_FilterByPriorityMarkComplete(self):
        self.taskMan.createTask("Task 1", "High")
        self.taskMan.createTask("Task 2", "High")
        self.taskMan.createTask("Task 3", "Medium")
        self.taskMan.markComplete("Task 2")
        self.taskMan.filterByPriority("High")
        self.assertEqual(len(self.taskMan.tasks), 3)
        self.assertEqual(self.taskMan.tasks[0].description, "Task 1")

    def test_CreateAndRemoveTask(self):
        self.taskMan.createTask("Test", "High")
        self.assertEqual(len(self.taskMan.tasks), 1)
        self.taskMan.removeTask("Test")
        self.assertEqual(len(self.taskMan.tasks), 0)
    
    def test_RemoveCompleteTask(self):
        self.taskMan.createTask("Test", "High")
        self.taskMan.markComplete("Test")
        self.taskMan.removeCompleteTask()
        self.assertEqual(len(self.taskMan.tasks), 0)
    
    def test_FilterTaskAfterMarkComplete(self):
        self.taskMan.createTask("Task 1", "Low")
        self.taskMan.createTask("Task 2", "Low")
        self.taskMan.createTask("Task 3", "Medium")
        self.taskMan.filterByPriority("High")
        self.assertEqual(len(self.taskMan.filteredTasks), 0)
        self.taskMan.markComplete("Task 3")
        self.taskMan.removeCompleteTask()
        self.taskMan.filterByPriority("Low")
        self.assertEqual(len(self.taskMan.tasks), 2)

    if __name__ == "__main__":
        unittest.main()
    
