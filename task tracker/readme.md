# Task Tracker CLI

A simple command-line task tracker written in Python. Tasks are stored locally in a `tasks.json` file, so no database or external service is required.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* List all tasks
* List completed tasks
* List tasks currently in progress
* Store task data in JSON
* Automatically record creation and update timestamps
* Validate task IDs
* Validate task statuses

## Requirements

* Python 3.x

The project uses only Python's standard library:

* `json`
* `datetime`
* `sys`

No external packages are required.

## Project Structure

```text
task-tracker/
│
├── task_tracker.py
├── tasks.json
└── README.md
```

`tasks.json` is created automatically when the application needs it and does not already exist.

## Task Format

Each task is stored as a JSON object:

```json
{
    "id": "1",
    "description": "Learn Python",
    "status": "todo",
    "created_at": "2026-09-27T19:30:00.123456",
    "updated_at": null
}
```

### Task Fields

| Field         | Description                          |
| ------------- | ------------------------------------ |
| `id`          | Unique identifier for the task       |
| `description` | Description of what needs to be done |
| `status`      | Current task status                  |
| `created_at`  | Time when the task was created       |
| `updated_at`  | Time when the task was last updated  |

### Valid Statuses

The application accepts these statuses:

```text
todo
in-progress
done
```

If an invalid status is supplied while adding a task, the application changes it to `todo`.

## Installation

Clone or download the project and enter its directory:

```bash
cd task-tracker
```

Then run the program with Python:

```bash
python task_tracker.py
```

## Commands

### 1. Add a Task

Syntax:

```bash
python task_tracker.py add <id> <description> <status>
```

Example:

```bash
python task_tracker.py add 1 "Learn Python" todo
```

Another example:

```bash
python task_tracker.py add 2 "Build CLI application" in-progress
```

The task ID must be unique.

If the supplied status is not one of:

```text
todo
in-progress
done
```

the status is automatically set to:

```text
todo
```

---

### 2. Update a Task

Syntax:

```bash
python task_tracker.py update <id> <description> <status>
```

Example:

```bash
python task_tracker.py update 1 "Learn Python and JSON" in-progress
```

The task must already exist.

When a task is updated, the `updated_at` timestamp is changed automatically.

If an invalid status is entered, the program asks for a valid status.

---

### 3. Delete a Task

Syntax:

```bash
python task_tracker.py delete <id>
```

Example:

```bash
python task_tracker.py delete 2
```

If the task ID does not exist, the program displays an error message.

---

### 4. List All Tasks

Syntax:

```bash
python task_tracker.py "list task"
```

Example output:

```text
ID : 1
Description: Learn Python
Status: todo
Created At: 2026-09-27T19:30:00.123456
Last Update At: None
```

The command is written inside quotes because `list task` contains a space.

---

### 5. List Completed Tasks

Syntax:

```bash
python task_tracker.py completed
```

This command is intended to display tasks whose status is completed.

> **Current implementation note:** The program's valid status is `done`, not `completed`. Therefore, the `completed` command currently checks for `"completed"` and will not find tasks with the normal `"done"` status. Change:
>
> ```python
> existing_task['status'] == "completed"
> ```
>
> to:
>
> ```python
> existing_task['status'] == "done"
> ```

---

### 6. List In-Progress Tasks

Syntax:

```bash
python task_tracker.py "in progress"
```

This displays tasks whose status is:

```text
in-progress
```

The command needs quotes because it contains a space.

---

### 7. Display Available Commands

Syntax:

```bash
python task_tracker.py "available command"
```

Output:

```text
AVAILABLE COMMANDS:
-------------------
add <id> <description> <status>
update <id> <description> <status>
delete <id>
list task
completed
in progress
available command
```

## Example Workflow

Create a task:

```bash
python task_tracker.py add 1 "Learn Python" todo
```

Start working on it:

```bash
python task_tracker.py update 1 "Learn Python" in-progress
```

Mark it as finished:

```bash
python task_tracker.py update 1 "Learn Python" done
```

View all tasks:

```bash
python task_tracker.py "list task"
```

View completed tasks:

```bash
python task_tracker.py completed
```

Delete the task:

```bash
python task_tracker.py delete 1
```

## Error Handling

The application handles several common errors.

### Missing Command

Running:

```bash
python task_tracker.py
```

produces a message asking for a command.

### Invalid Command

For example:

```bash
python task_tracker.py hello
```

produces:

```text
INVALID COMMAND.
```

### Duplicate Task ID

Trying to add a task with an existing ID produces:

```text
THE TASK ID ALREADY EXISTS. PLEASE ENTER ANOTHER TASK ID
```

### Nonexistent Task

Updating or deleting a nonexistent task produces an error message.

### Invalid JSON

If `tasks.json` contains invalid JSON, the program reports the file as invalid rather than attempting to process it.

## Important Command-Line Note

Commands containing spaces must currently be enclosed in quotes.

Use:

```bash
python task_tracker.py "list task"
```

instead of:

```bash
python task_tracker.py list task
```

Similarly:

```bash
python task_tracker.py "in progress"
```

and:

```bash
python task_tracker.py "available command"
```

## Known Implementation Issues

The current implementation has a few issues that should be addressed as the project develops.

### 1. `completed_tasks()` checks the wrong status

Valid statuses are:

```text
todo
in-progress
done
```

but `completed_tasks()` checks:

```python
existing_task['status'] == "completed"
```

It should use:

```python
existing_task['status'] == "done"
```

### 2. `else` belongs to the `for` loop

In both `completed_tasks()` and `inprogress_tasks()`, the code currently has:

```python
for existing_task in tasks:
    if ...:
        ...
else:
    print("NO TASK ...")
```

The `else` executes after the entire `for` loop finishes, not only when the `if` condition fails.

This can cause:

```text
NO TASK COMPLETED YET
```

to be printed even when completed tasks were found.

A better approach is to use a flag or build a filtered list of matching tasks.

### 3. `updated_at` is initially `None`

New tasks have:

```python
"updated_at": None
```

This is reasonable, but `list_tasks()` assumes the field always exists. If the JSON file is manually modified and the field is missing, the program can raise a `KeyError`.

### 4. Command parsing can be improved

The program currently treats the first command-line argument as the command:

```python
command = sys.argv[1]
```

This makes multi-word commands require quotes.

A more conventional CLI design would use commands such as:

```bash
python task_tracker.py list
python task_tracker.py in-progress
python task_tracker.py available
```

This would make the command-line interface easier to use.


project url : [https://github.com/Sudeeppaneru/python-projects-programs](https://roadmap.sh/projects/task-tracker)
