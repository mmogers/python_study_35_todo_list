import time, os

def viewList():
  os.system("clear")
  if len(toDoList) > 0:
    for index in range(len(toDoList)):
      print(f"{index+1} : {toDoList[index]}")
  else:
    print("The To Do List is empty!")
  time.sleep(2)

def addToList():
  print("What do you want to add: ")
  item  = input("").lower()
  if item in toDoList:
    print(f"The - {item} - already exists in a list ")
  else:
    toDoList.append(item)
  time.sleep(2)

def editList():
  print("Here is a list")
  viewList()
  print("Which item do you want to change: ")
  index = int (input(""))
  if index > len(toDoList):
    print("The index is out of the range! ")
  else:
    task = input("What task do you want to add instead: ")
    if task in toDoList:
      print(f"The task - {task} - is already in the list!")
    else:
      toDoList[index-1] = task 
  time.sleep(2)  

def removeFromList():
  print("Do you want to remove the whole list? Yes/No: ")
  removeList = input("").lower()
  if removeList == "yes": 
    confirmation = input ("are you sure? Yes/No: ") 
    if confirmation == "yes":
      toDoList.clear()
      print("The list was removed!")
    else:
      print("The list was not deleted!")
  elif removeList == "no":
    print("Here is a list")
    viewList()
    print("What do you want to remove: ")
    task = input("")
    if task in toDoList:
      print("\nAre you sure you want to remove this? Yes/No: ")
      confirmation = input("").lower()
      if confirmation == "yes":
        toDoList.remove(task)
        print(f"The task - {task} - was removed successfully!")
      else:
        print(f"The task - {task} - will not be removed!")
    else:
      print("There is no such task in To Do List!")
  else:
    print("There is no such answer option!")
  time.sleep(2)

toDoList = []
while True: 
  os.system("clear")
  print("\033[1;32m \U00002705 To Do List Manager:\033[0m \U00002705")
  print("Do you want to view, add, edit, or remove an item from the to do list?")
  command = input("").lower()

  if command == "view":
    viewList()
  elif command == "add":
    addToList()
  elif command == "edit":
    editList()
  elif command == "remove":
    removeFromList()
  else:
    print("There is no such command!")
    time.sleep(2)