# PyQuizT

PyQuizT is a software project developed for the "Software Engineering Principle" course at the Department of Computer Engineering, School of Engineering, KMITL. This project aims to create an interactive quiz management system with a user-friendly interface.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

PyQuizT is a Python application built with PyQt6 for the graphical user interface and FastAPI for the backend service. The system allows users to create courses, manage quizzes, and view analytics related to quiz performance. It also ensures secure user authentication and data storage.

## Features

- **User Management:**
  - Create, join, and own courses.
  - Manage participants in courses.
  - Secure user authentication with password hashing.

- **Quiz Management:**
  - Create quizzes with different question types.
  - Set deadlines for quizzes.
  - Automatically score multiple-choice and checkbox answers.

- **Analytics and Statistics:**
  - View course minimum, maximum, and mean scores.
  - Display analytical charts for quiz performance.

- **Data Storage:**
  - Use ZODB (Zope Object Database) for storing Python objects directly.

- **Cross-Platform Support:**
  - Developed with PyQt6, ensuring compatibility with Windows, Mac, and Linux.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/PyQuizT.git
   cd PyQuizT
   ```

2. Install dependencies:
      ```
      pip install -r requirements.txt
      ```

## Usage
Run the application:

      ```
      python3 main.py
      ```


## Folder Structure

PyQuizT/
|-- app/
|   |-- main.py
|   |-- views/
|-- data/
|-- model/
|-- utils/
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- venv/


app: Contains the main application code.
data: Handles data-related functionalities.
model: Contains classes representing the data model of the application.
utils: Holds utility functions.
requirements.txt: Lists required Python packages.
README.md: Project documentation.
.gitignore: Specifies files and directories to ignore in version control.

## Dependencies
PyQt6
FastAPI
Pydantic
ZODB
bcrypt
QtCharts (PyQt6-QtCharts or PySide6-QtCharts)
Contributing
Contributions are welcome! Please follow the CONTRIBUTING.md guidelines.

## License
This project is licensed under the MIT License.