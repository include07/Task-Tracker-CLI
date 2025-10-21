# Task-Tracker-CLI

A simple command-line tool for tracking tasks using Python and Typer, part of the roadmap.sh guide https://roadmap.sh/projects/task-tracker

## Features

- Add, list, update, and delete tasks
- Mark tasks as done or in progress
- Filter tasks by status
- Stores tasks in a local JSON file

## Requirements

- Python 3.8 or newer
- [pip](https://pip.pypa.io/en/stable/)

## Project Structure

```
Task-Tracker-CLI/
├── pyproject.toml
├── tasks.json
└── task_tracker/
    └── task_tracker.py
```

- The main CLI logic is in `task_tracker/task_tracker.py`.
- The CLI tool is installed and made available as `task-cli` via the entry point defined in `pyproject.toml`.
- All commands (add, list, update, delete, mark-done, mark-in-progress) are implemented in this file.
- Tasks are stored in `tasks.json` in the project root.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Task-Tracker-CLI.git
   cd Task-Tracker-CLI
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the tool in editable mode:**
   ```bash
   pip install -e .
   ```

## Usage

After installation, use the `task-cli` command:

- **Add a task:**
  ```bash
  task-cli add "Buy groceries"
  ```

- **List all tasks:**
  ```bash
  task-cli list
  ```

- **List tasks by status:**
  ```bash
  task-cli list done
  task-cli list todo
  task-cli list in-progress
  ```

- **Mark a task as done:**
  ```bash
  task-cli mark-done 1
  ```

- **Mark a task as in progress:**
  ```bash
  task-cli mark-in-progress 1
  ```

- **Delete a task:**
  ```bash
  task-cli delete 1
  ```

- **Show help:**
  ```bash
  task-cli --help
  ```

## Notes

- All tasks are stored in `tasks.json` in the project directory.
- Make sure your virtual environment is activated when using the tool. If you open a new terminal, run `source .venv/bin/activate` before using `task-cli`.

## License

MIT
