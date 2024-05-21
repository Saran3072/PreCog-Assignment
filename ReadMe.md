# Project Setup Instructions

This document guides you through the process of setting up your development environment for this project.

## Prerequisites

Before you begin, ensure you have git installed on your system. You will also need Python and the ability to create virtual environments.

## Cloning the Repository

To clone the repository, open a terminal and run the following command:

```
git clone https://github.com/Saran3072/PreCog-Assignment.git
```

## Navigating into the Repository

After cloning the repository, navigate into the directory:

```
cd <repository-name>
```
Replace `<repository-name>` with the name of the folder that was created when you cloned the repository.

## Setting Up the Python Environment

Create a Python virtual environment to manage the dependencies locally by running:

```
python -m venv env
```

## Activating the Python Environment

Activate the virtual environment with the following command:

### On Windows:
```
env\Scripts\activate
```

### On macOS and Linux:
```
source env/bin/activate
```

## Installing Dependencies

Install all required dependencies using the following command:

```
pip install -r Requirements.txt
```

After completing these steps, you should have a fully configured environment to work on the project.

Here's a README document with the instructions for executing Task-1, Task-2, and the Bonus Task, written in plain text without Markdown formatting:

---

**Project Execution Instructions**

This document provides detailed instructions on how to execute various tasks within this project.

**Executing Task-1:**

1. **Navigate to Task-1 Directory:**
Enter the command: 
```
cd Task-1
```

2. **Create Directories:**
Create directories called 'plots' and 'properties' by entering:
   ```
   mkdir plots properties
   ```

3. **Run the Main Script:**
Execute the script with:
```
python main.py
```

**Executing Task-2:**

1. **Navigate to Task-2 from Home Directory:**
Enter the command:
```
cd Task-2
```

2. **Create Directories:**
Create directories for storing data with:
```
mkdir graphs plots
```

3. **Create Subdirectories under Plots:**
Navigate into plots:
```
cd plots
```
Create directories called 'girvan' and 'louvain':
```
mkdir girvan louvain
```
Return to Task-2 directory:
```
cd ..
```

4. **Run the Main Script:**
Execute the script with:
```
python main.py
```

**Running Bonus Task:**

*Node2Vec:*

1. **Navigate to the Node2Vec Directory:**
Enter the command: 
```
cd Bonus-Task/Node2Vec
```

2. **Run the Main Script:**
Execute the script with:
```
python main.py
```

*GNN:*

1. **Navigate to the GNN Directory:**
Enter the command:
```
cd Bonus-Task/GNN
```

2. **Run the Main Script:**
Execute the script with:
```
python main.py
```
