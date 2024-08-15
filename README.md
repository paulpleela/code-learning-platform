# Code Learning Platform

PyQuiz is a code learning platform designed to create an interactive and practical learning experience. The program allows teachers to create and manage online courses. Students can enroll in courses, access learning materials, and attempt Python coding quizzes (which will automatically be checked against test cases). 


## Features

### Course Management

* **User Roles:** Users can select a role (either teacher or student) during registration. Teachers can create and manage course content. Students can enroll in courses (with a course code) to access content, complete quizzes, and track their progress.
* **Course Modules:** Modules within a course allow teachers to organize and manage course content by grouping learning materials and quizzes by topic. Teachers can also set module deadlines, after which learning materials and quizzes will be unavailable to students.
* **Learning Materials:** Teachers can upload learning materials, including PDF files and MP4 videos, into the course modules. Students can view learning materials directly on the app. 
* **Coding Quizzes:** Teachers can create Python coding quizzes in the course modules by entering questions and test cases. Students can write and run their code with the built-in code editor. Submitted code will automatically be checked against the test cases, providing instant feedback.

### Progress Tracking

* **Module Deadlines Calendar:** Students can view a weekly calendar of the course modules that will be due. Teachers can see a calendar of their assigned modules' deadlines.
* **Course Progress Dashboard:** Students can see a summary of their enrolled courses. Each course's progress bar shows the percentage of modules completed.
* **Course Completion Certificates:** When a student successfully completes all available modules of a course, they will be able to view and download a personalized certificate.


## Technologies Used

* **Python:** Program functionality and logic
* **PyQt6:** Graphical user interface
* **FastAPI:** RESTful backend service
* **ZODB:** Object-oriented database


## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (version 3.8 or higher)
- [Pip](https://pip.pypa.io/en/stable/installation/)

### Installing and Running the Application

1. Clone this repository:

    ```bash
    git clone https://github.com/paulpleela/code-learning-platform.git
    ```

2. Navigate to the project directory:

    ```bash
    cd code-learning-platform
    ```
    
3. Set up and activate a virtual environment (Optional):

    ```sh
    python -m venv venv
    ```
    
    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Run the backend server:

    ```bash
    cd server
    uvicorn main:app
    ```  

6. Run the application:

    ```bash
    cd app
    python main.py
    ```  


## Contributors

- Parisorn Prasartkul
- Peeranat Leelawattanapanit
- Soe Moe Htet


## License

[MIT](https://choosealicense.com/licenses/mit/)
