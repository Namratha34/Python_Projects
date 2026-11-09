#TO - DO LIST APPLICATION
#WELCOME YOU ALL
tasks = []
print("TO-DO LIST APPLICATION\n")
print("WELCOME YOU")

def add_task():
    task = input("Enter your task:\n")

    task_dict = {
        "name": task,
        "completed": False
    }

    tasks.append(task_dict)

    print("Task added successfully!")

    
def  view_task():
    if tasks:
        for index,task in enumerate(tasks,start=1):
            print(task["name"])
            print(task["completed"])
    else:
        print("No Tasks has been added so far:")

def mark_as_completed():
    if tasks:
        for index,task in enumerate(tasks,start=1):
            print(index,task)
    mark=int(input("Enter which task should be marked as completed:"))


def  delete_task():
    pass






while True:
    print("ADD TASK:\n")
    print("VIEW TASKS\n")
    print("MARK TASK AS COMPLETED\n")
    print("DELETE TASK\n")
    print("EXIT")
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
            break
        case _:
            print("Ivalid choice please enter valid choice 1/2/3/4/5")

