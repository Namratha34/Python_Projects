#TO - DO LIST APPLICATION
#WELCOME YOU ALL
import json
tasks = []
print("*****========================================*****")
print("*****TO-DO LIST APPLICATION\n*****")
print("*****WELCOME YOU*****")

def add_task():
    task = input("Enter your task:\n")

    if not task.strip():
        print("Task name cannot be empty!!")
        return

    task_dict = {
        "name": task,
        "completed": False
    }

    tasks.append(task_dict)
    save_tasks()

    print("Task added successfully!")

    
def  view_task():
    if tasks:
        for index,task in enumerate(tasks,start=1):
            if task["completed"] == True:
                status = "completed"
            else:
                status = "pending"
            print(f"{index}.{task['name']}-{status}")
    else:
        print("No Tasks has been added so far:")

def mark_as_completed():
    if tasks:
        for index,task in enumerate(tasks,start=1):
            print(index,task["name"])
        mark=int(input("Enter which task should be marked as completed:"))
        if mark>=1 and mark<=len(tasks):
            mark = mark-1
            tasks[mark]["completed"] = True
            save_tasks()
            print("Task marked as completed successfully!!!")
        else:
            print("Invalid task number!!")
    


def  delete_task():
    if tasks:
        for index,task in enumerate(tasks,start=1):
                    print(index,task["name"])
        delete=int(input("Enter which task you want to delete")) 
        
        if delete >=1 and delete <=len(tasks):
            tasks.pop(delete - 1)
            print("Tasks delted successfully!!")
            save_tasks()
        else:
            print("Invalid task number!")
    else:
            print("No tasks avaialable to delete..")

def update_task():
    if tasks:
        for index,task in enumerate(tasks,start=1):
            print(index,task["name"])
        task_num = int(input("Enter the task number to update exisiting tasks"))
        if task_num>=1 and task_num<=len(tasks):
            task_num = task_num-1
            new_task = input("Enter the new task!!")

            if not new_task.strip():
                print("Task number cannot be empty!")
                return
            tasks[task_num]["name"] = new_task
            print("Task updated successfully!!")
            save_tasks()
        else:
            print("Invalid task number")

    else:
        print("No tasks available to update!")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully!")

def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []
        print("Invalid JSON file. Starting with an empty task list.")

load_tasks()

while True:
    print("1.ADD TASK:")
    print("2.VIEW TASKS:")
    print("3.MARK TASK AS COMPLETED:")
    print("4.DELETE TASKS:")
    print("5.UPDATE TASKS:")
    print("6.EXIT:")
    choice=int(input("Enter your choice:1/2/3/4/5:\n"))

    match choice:
        case 1:
            add_task()
        case 2:
            view_task()
        case 3:
            mark_as_completed()
        case 4:
            delete_task()
        case 5:
            update_task()
        case 6:
            save_tasks()
        case 7:
            load_tasks()
        case 8:
            save_tasks()
            print("THANK YOU FOR USING TO DO LIST APPLICATION....")
            break

        case _:
            print("Ivalid choice please enter valid choice 1/2/3/4/5/6/7/8")

