#To-Do list using CLI in Python

import os #used to check availability of tasks file
import json #used to save tasks in a file

task_file = "tasks.json"
def add_task(tasks): #used to add a new task into file
    task = input("Enter task: ")
    task_dict = {"id": len(tasks)+1,
                 "task": task,
                 "completed": False}
    tasks.append(task_dict)
    save_task(tasks)
    print('Task saved sucessfully...')
def del_task(tasks): #used to delete a task
    task_id = int(input("Enter task id to delete: "))
    if(1<=task_id<=len(tasks)):
        tasks.pop(task_id-1)
        save_task(tasks)
        print(f"Task with {task_id} has been deleted sucessfully...")
    else:
        print('No Task found. Try again.')
def view_task(tasks): #used to print all tasks
    
    if not tasks:
        print("No tasks added.")
        return
    
    i = 1
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['task']} {status}")
        i = i+1
def mark_task(tasks): #used to mark a task as finished
    task_id = int(input("Enter Task id to mark as done: "))
    i = 1
    for task in tasks:
        if task_id == i:
            task["completed"] = True
            print("Task marked as done...")
        else:
            i = i+1
def get_task(): #used to import tasks into program
    if os.path.exists(task_file):
        try:
            with open(task_file, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading tasks: {e}")
            return []
        return []
def save_task(tasks): #used to save tasks file after modifying
    with open(task_file, "w") as f:
        json.dump(tasks, f)
def main():
    tasks = get_task()
    while True:
        print('\n---TO-DO LIST MENU---\n')
        print('1. Add Task\n')
        print('2. Delete Task\n')
        print('3. View Tasks\n')
        print('4. Mark Task as Done')
        print('5. Exit')
        
        choice = int(input("Enter your choice from 1-5: "))

        if(choice==1):
            add_task(tasks)
        elif(choice==2):
            del_task(tasks)
        elif(choice==3):
            view_task(tasks)
        elif(choice==4):
            mark_task(tasks)
        elif(choice==5):
            break
        else:
            print('Invalid Choice. Try again.')
main()