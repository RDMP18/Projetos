#####################################################################################
#                                  PROJECT Nº2                                      #
#                                   TASK LIST                                       #
#####################################################################################

# IMPORTANT: Please run the script inside the /toDoList directory. Thank you.

import json
import os

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
    if not toDoList:
        print("No tasks on your To Do List!")
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
    global toDoList
    toDoList = [task for task in toDoList if task["id"] != id]
    print(f"Task with ID {id} successfully removed!")

def removeAllCompletedTasks():
    global toDoList
    toDoList = [task for task in toDoList if task["status"] != "completed"]
    print(f"All completed tasks were removed!")

def saveTasks():
    global toDoList
    try:
        os.mkdir("savefiles")
    except:
        print("Save files directory already exists! Moving on...")
    finally:
        og = str(os.getcwd())
        path = og + "\\savefiles"
        title = input("Choose a name for you save file: ") + ".json"
        os.chdir(path)
        file = open(title, "w")
        json.dump(toDoList, file, indent = 4)
        file.close()
        os.chdir(og)


def loadTasks():
    global toDoList

    if not os.path.isdir("savefiles"):
        print("There are no save files to load! Moving on...")

    else:
        og = str(os.getcwd())
        path = og + "\\savefiles"
        print("Here are all available savefiles.")
        directories = os.listdir("savefiles")
        for i in range(len(directories)):
            print(f"{i}. {directories[i]}")
        choice = int(input("Please, choose which savefile you wish to load (BE WARNED, THIS WILL OVERWRITE THE VALUES OF THE CURRENT TO-DO LIST): "))
        try:
            os.chdir(path)
            file = open(directories[choice], "r")
            toDoList = json.load(file)
            file.close()
            os.chdir(og)
        except:
           print("Invalid choice. Moving on...")

def menu():
    while 1:
        print("TO-DO LIST")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Flag task as \"completed\"")
        print("4. Remove task")
        print("5. Remove all completed tasks")
        print("6. Save To Do List")
        print("7. Load To Do List")
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
        elif choice == 4:
            id = int(input("Which task would you like to remove? (Please insert the ID): "))
            removeTask(id)
        elif choice == 5:
            removeAllCompletedTasks()
        elif choice == 6:
            saveTasks()
        elif choice == 7:
            loadTasks()
        else:
            print("Thank you for using my services. Goodbye!")
            break


if __name__ == "__main__":
    menu()

# Brought to you by RDMP18