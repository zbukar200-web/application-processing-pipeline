# Application Processing Pipeline

## Assignment Overview
This project is a mini **Application Processing Pipeline** built in Python for a data structures practice task.

The program simulates how startup applications move through a simple approval system using:

- a **Queue (FIFO – First In, First Out)** for incoming applications
- a **Stack (LIFO – Last In, First Out)** for tracking processed applications

It also demonstrates how the most recent approval can be reversed if a mistake occurs.



## What the App Does

This Python program performs the following steps:

1. Imports `deque` from Python’s `collections` module
2. Creates:
   - an empty queue called `application_inbox`
   - an empty stack called `processed_history`
3. Stores a list of 4 messy startup names:
   - `" TechCorp "`
   - `"bio-gen"`
   - `"  GreenSpark  "`
   - `"AI Nexus "`
4. Cleans each startup name by:
   - removing extra spaces using `.strip()`
   - converting text to lowercase using `.lower()`
5. Adds the cleaned names into the queue
6. Processes the applications in **FIFO order** using `popleft()`
7. Prints each approved application
8. Stores approved applications in the stack
9. Simulates an error by removing the most recent approval using `pop()`
10. Prints which application was reverted

In simple terms, the app shows how a real system can:
- receive applications in order,
- process them one by one,
- and undo the latest action if a mistake happens.


## Concepts Demonstrated

This project demonstrates:

- `deque` from `collections`
- Queue operations:
  - `append()`
  - `popleft()`
- Stack operations:
  - `append()`
  - `pop()`
- String cleaning:
  - `.strip()`
  - `.lower()`
- `for` loops
- `while` loops
- Conditional statements (`if`)
- Basic Python data structure workflow


## Project Files

- `app_pipeline.py` → Main Python program
- `README.md` → Project documentation and beginner-friendly instructions


## How to Run the App Locally (Beginner Friendly)

Follow these steps carefully:

### Step 1: Download the project
You can either:

- **Download the ZIP file** from GitHub  
or
- **Clone the repository** using Git

If using Git, run:

```bash
https://github.com/zbukar200-web/application-processing-pipeline.git
