# Project Setup Instructions

This document guides you through the process of setting up your development environment for this project.

## Prerequisites

Before you begin, ensure you have git installed on your system. You will also need Python and the ability to create virtual environments.

## Cloning the Repository

To clone the repository, open a terminal and run the following command:

```
git clone <repository-link>
```
Replace `<repository-link>` with the actual URL of the repository.

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