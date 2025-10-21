import typer
import json
from datetime import datetime
from pathlib import Path

def ensure_tasks_file_exists():
    """
    Ensure that the tasks.json file exists.
    If it does not exist, create it.
    """
    file_path = Path('tasks.json')
    if not file_path.exists():
        file_path.touch()
        
def load_tasks() -> list:
    """
    Read tasks from the JSON file.
    This function opens the tasks.json file in read mode and parses its contents as JSON.
    It returns a list of task dictionaries if successful.
    If the file doesn't exist or contains invalid JSON, it returns an empty list.
    Returns:
        list: A list of task dictionaries if the file is valid, otherwise an empty list.
    """
    file_path = "tasks.json"
    with open(file_path, 'r') as file:
        tasks = json.load(file)
        return tasks

def get_last_id() -> int:
    """
    Retrieves the highest task ID from the list of loaded tasks.
    This function loads all tasks using the `load_tasks()` function and determines the maximum value of the 'id' field among them.
    If there are no tasks, it returns 0.
    Returns:
        int: The highest task ID if tasks exist, otherwise 0.
    """
    tasks = load_tasks()
    if not tasks:
        return 0
    return max(task['id'] for task in tasks)

def task_exists(id: int) -> bool:
    """
    Check if a task exists by its ID.
    """
    tasks = load_tasks()
    return any(task['id'] == id for task in tasks)

ensure_tasks_file_exists()

app = typer.Typer()

@app.command()
def add(description: str):
    """
    Add a new task
    """
    tasks = load_tasks()
    new_id = get_last_id() + 1
    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": description,
        "status": "pending",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    typer.echo(f"Task added successfully (ID: {new_id})")

@app.command()
def delete(id: int):
    """
    Delete a task by its ID
    """
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != id]
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    typer.echo(f"Task ID {id} deleted successfully.")

@app.command()
def update(id: int, description: str):
    """
    Update a task's description by its ID
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            typer.echo(f"Task ID {id} updated successfully.")
            return
    typer.echo(f"Task ID {id} not found.")

@app.command()
def mark_done(id: int):
    """
    Mark a task as done by its ID
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            typer.echo(f"Task ID {id} marked as done.")
            return
    typer.echo(f"Task ID {id} not found.")

@app.command()
def mark_in_progress(id: int):
    """
    Mark a task as in progress by its ID
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'in progress'
            task['updatedAt'] = datetime.now().isoformat()
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            typer.echo(f"Task ID {id} marked as in progress.")
            return
    typer.echo(f"Task ID {id} not found.")

@app.command()
def list(status: str = typer.Argument(None, help="Filter tasks by status: done, todo, in-progress")):
    """
    List all tasks or filter by status
    """
    tasks = load_tasks()
    if not tasks:
        typer.echo("No tasks found.")
        return
    
    # Define status mappings
    status_map = {
        "done": "done",
        "todo": "pending",
        "in-progress": "in-progress"
    }
    
    if status and status in status_map:
        filtered_tasks = [task for task in tasks if task['status'] == status_map[status]]
        if not filtered_tasks:
            typer.echo(f"No tasks found with status '{status}'.")
            return
        tasks = filtered_tasks
    elif status:
        typer.echo(f"Invalid status: {status}. Use 'done', 'todo', or 'in-progress'.")
        return
    
    for task in tasks:
        typer.echo(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")


if __name__ == "__main__":
    app()