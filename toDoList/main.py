import json

toDoList = []

def createTask(description):
    global toDoList
    toDo = {
        "id": len(toDoList) + 1,
        "description": description,
        "status": "pending"
    }
    toDoList.append(toDo)
    print(f"Task with '{description}' added to the list!")

def listAllTasks():
    global toDoList
    for task in toDoList:
        status = "X" if task["status"] == "completed" else "O"
        print(f"[{status}] ID {task["id"]}: {task["description"]}")

def completeTask(id):
    global toDoList
    for task in toDoList:
        if task["id"] == id:
            task["status"] = "completed"
            print(f"Task {id} completed!")
            return
    print(f"Task {id} was not found!")

def removeTask(id):
    pass

def saveTasks():
    pass

def loadTasks():
    pass

def menu():
    while 1:
        print("TO-DO LIST")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Flag task as \"completed\"")
        print("4. Remove task")
        print("5. Remove all completed tasks")
        print("0. Exit")

        try:
            choice = int(input("Choose a number: "))
        except ValueError:
            print("Choice invalid! Please, choose again.")
            continue

        if choice == 1:
            description = input("Please, input the description of your new task: ")
            createTask(description)
        elif choice == 2:
            listAllTasks()
        elif choice == 3:
            id = int(input("Which task would you like to complete? (Please insert the ID): "))
            completeTask(id)
        else:
            print("Bye!")
            break


if __name__ == "__main__":
    menu()