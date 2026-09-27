import json
import datetime
import sys

def valid_task(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        with open("tasks.json", "w") as file:
            json.dump([], file)
        return False

    except json.JSONDecodeError:
        return False

    return any(t["id"] == task_id for t in tasks)

def status_input_validation(task):
    valid_status = ("todo" , "in-progress" , "done")
    if task["status"] in valid_status:
        return True
    False

def add_task(task):
    if len(sys.argv) < 5:
        print("PLEASE ENTER ALL THE PARAMETERS")

    if valid_task(task["id"]):
        print("THE TASK ID ALREADY EXISTS. PLEASE ENTER ANOTHER TASK ID")
        return
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    if not status_input_validation(task): task["status"] = "todo"
    task["created_at"] = datetime.datetime.now().isoformat()
    tasks.append(task)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
    return

def update_task(task):
    if len(sys.argv) < 5:
        print("PLEASE ENTER ALL THE PARAMETERS")
    if not valid_task(task["id"]):
        print("THE ID DOESN'T EXIST")
        return
    
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("INVALID JSON OR FILE DOESN'T EXIST")
        return

    for existing_task in tasks:
        if existing_task["id"] == task["id"]:

            for key in task:
                if key != "id" and task[key] is not None:
                    if key == "status":
                        while not status_input_validation({"status": task[key]}):
                            print("Enter a valid status:")
                            print("1.todo \n 2.in-progress 3.done")
                            task[key] = input("PLEASE ENTER STATUS HERE:")
                    existing_task[key] = task[key]


            existing_task["updated_at"] = datetime.datetime.now().isoformat()
            break

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return


def delete_task(task):
    if not valid_task(task["id"]):
        print("THE TASK DOESN'T EXIST")
        return

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("INVALID JSON OR FILE DOESN'T EXIST")
        return
    
     
    count = 0
    for existing_task in tasks:
        count += 1 
        if existing_task["id"] == task["id"]:
            delete_index = count - 1 

    tasks.pop(delete_index)

    try:
        with open("tasks.json", "w") as file:
            tasks = json.dump(tasks , file, indent = 4)

    except (FileNotFoundError, json.JSONDecodeError):
        print("INVALID JSON OR FILE DOESN'T EXIST")
        return

def list_tasks(task):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

            if not tasks:
                print("NO TASK. ADD TASKS TO SEE THE TASKS")
            else:
                for existing_task in tasks:
                    print(f"ID : {existing_task['id']}")
                    print(f"Description: {existing_task['description']}" )
                    print(f"Status: {existing_task['status']}")
                    print(f"Created At: {existing_task['created_at']}")
                    print(f"Last Update At: {existing_task['updated_at']} \n")
    except (FileNotFoundError, json.JSONDecodeError): 
        print("INVALID JSON OR FILE NOT FOUND")
        return
    


def completed_tasks(task):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

            if not tasks:
                print("NO TASK. ADD TASKS TO SEE THE TASKS")
            else:
                for existing_task in tasks:
                    if existing_task['status'] == "completed":
                        print(f"ID : {existing_task['id']}")
                        print(f"Description: {existing_task['description']}" )
                        print(f"Status: {existing_task['status']}")
                        print(f"Created At: {existing_task['created_at']}")
                        print(f"Last Update At: {existing_task['updated_at']} \n")
                else:
                    print("NO TASK COMPLETED YET")
    except (FileNotFoundError, json.JSONDecodeError): 
        print("INVALID JSON OR FILE NOT FOUND")
        return
    


def inprogress_tasks(task):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

            if not tasks:
                print("NO TASK. ADD TASKS TO SEE THE TASKS")
            else:
                for existing_task in tasks:
                    if existing_task['status'] == "in-progress":
                        print(f"ID : {existing_task['id']}")
                        print(f"Description: {existing_task['description']}" )
                        print(f"Status: {existing_task['status']}")
                        print(f"Created At: {existing_task['created_at']}")
                        print(f"Last Update At: {existing_task['updated_at']} \n")
                else:
                    print("NO TASK IN-PROGRESS YET")
    except (FileNotFoundError, json.JSONDecodeError): 
        print("INVALID JSON OR FILE NOT FOUND")
        return
    

def command_available(task):
    print("\nAVAILABLE COMMANDS:")
    print("-------------------")
    print("add <id> <description> <status>")
    print("update <id> <description> <status>")
    print("delete <id>")
    print("list task")
    print("completed")
    print("in progress")
    print("available command")


def check_arguments_length():

    if len(sys.argv) < 2:
        print("PLEASE PROVIDE COMMAND TO PERFORM OPERATION.")
        print(
            'YOU CAN SEE AVAILABLE COMMANDS USING:\n'
            'python task_tracker.py "available command"'
        )
        return

    check_command()


def check_command():

    command = sys.argv[1]

    task = {
        "id": None,
        "description": None,
        "status": None,
        "created_at": None,
        "updated_at": None
    }

    keys = list(task.keys())

    for i, argument in enumerate(sys.argv[2:]):

        if i >= len(keys):
            print("TOO MANY ARGUMENTS PROVIDED.")
            return

        task[keys[i]] = argument

    command_function_directory = {
        "add": add_task,
        "update": update_task,
        "delete": delete_task,
        "list task": list_tasks,
        "completed": completed_tasks,
        "in progress": inprogress_tasks,
        "available command": command_available
    }

    if command not in command_function_directory:
        print("INVALID COMMAND.")
        return

    command_function_directory[command](task)


check_arguments_length()