from datetime import date, datetime 
now = datetime.now()
formatted = now.strftime("%H:%M:%S, %m-%d-%Y")
print(f"Welcome to BS' Calendar! It is {formatted}.")

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['description']} - {status}")

    def mark_task_complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
        else:
            print("Invalid task index dumbass")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index-1]
            print("Task removed")
        else:
            print("Invalid task index dumbass")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Leave")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
            print("You're welcome.")

        if choice == "2":
            todo_list.view_tasks()

        if choice == "3":
            index = int(input("Which task did you complete? "))
            todo_list.mark_task_complete(index)
            print("Good job dude")

        if choice == "4":
            index = int(input("Now which task did you fuck up? "))
            todo_list.remove_task(index)
            print("Apologize for being stupid")
            while True:
                apologize = input("""Write "I'm sorry Ben, for being so stupid" here: """)
                if apologize == "I'm sorry Ben, for being so stupid":
                       print("That's right, don't do it again.")
                       break
        if choice == "5":
            please = input('Say "Please": ')
            while True:
                if please == "Please":
                    break
            print("Learn your manners and don't come back. You stink btw.")
            break

if __name__ == "__main__":
    main()