import datetime
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict
import os, sys
from ZODB import FileStorage, DB

app = FastAPI()


from database import *

code_generator = CourseCodeGenerator()
db_helper = ZODBHelper('mydatabase.fs')
 
 # Base model for student registration, login, and course creation

class UserRegister(BaseModel):
    username: str
    password: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str


class CourseCreated(BaseModel):
    courseName: str
    teacherName: str

class Module(BaseModel):
    moduleName: str
    moduleDescription: str
    moduleLessonList: list
    moduleQuestionsList: list
    moduleDueDate: datetime.datetime
    moduleType: str
    moduleStatus: str

class Lesson(BaseModel):
    lessonName: str
    lessonDescription: str
    lessonContent: str
    lessonType: str
    lessonStatus: str

class Question(BaseModel):
    questionName: str
    questionText: str
    questionType: str
    questionOptions: list
    questionAnswer: str

class Submission(BaseModel):
    submissionName: str
    submissionContent: str
    submissionStatus: str

class testCase(BaseModel):
    testCaseName: str
    testCaseInput: str
    testCaseOutput: str
print("------------------------------   Server running......    ------------------------------")

@app.post("/api/user/register")
async def register_user(user: UserRegister):

    if user.role == "student":
        if db_helper.user_authentication.student_exists(user.username):
            raise HTTPException(status_code=400, detail="This username is taken")
    
    elif user.role == "teacher":
        if db_helper.user_authentication.teacher_exists(user.username):
            raise HTTPException(status_code=400, detail="This username is taken")
    db_helper.user_registration.register_user(user)

    return {"message": "user registered successfully"}

@app.post("/api/user/login")
async def login_user(user: UserLogin):
    print("Login user", user.username, user.password)
    # Use username to search for the student in the database
    user = db_helper.user_authentication.login_user(user.username, user.password)
    db_helper.user_authentication.get_user_details()

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"message": "Login successful", "username": user.name}

'''----------------------------------    Course      ---------------------------------- 
    '''
@app.post("api/teacher/course")
async def course(course: CourseCreated):
    course_code = code_generator.generate_code()
    course_created_date = datetime.datetime.now()
    course = Course(course.courseName, course_created_date, course_code, course.teacherName, [], [], [])

    db_helper.course_operations.create_course(course, course.teacherName)


        
    return {"message": "Course created successfully"}

# get operation
@app.get("/courses")
async def get_allcourses():
    courses = db_helper.course_operations.get_all_courses()
    return {"courses": courses}    

@app.get("/course/{courseCode}")
async def get_course(courseCode: str):
    course = db_helper.course_operations.get_course_by_code(courseCode)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course

@app.get("api/teacher/ownedCourses/{teacherName}")
async def get_owned_courses(teacherName: str):
    ownedCourses = db_helper.course_operations.get_courses_by_teacher(teacherName)
    return {"courses": ownedCourses}

# update operation 
@app.put("/course/{courseCode}")
async def update_course(courseCode: str, course: CourseCreated):
    db_helper.course_operations.update_course(courseCode, course)

@app.delete("/course/{courseName}")
async def delete_course(courseName: str):
    existing_course = db_helper.get_course(courseName)
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    db_helper.delete_course(courseName)

    return {"message": "Course deleted successfully"}

'''----------------------------------    Module      ---------------------------------- '''
@app.post("/module")
async def create_module(module: Module):
    db_helper.module_operations.create_module(module)



    return {"message": "Module created successfully"}

@app.get("/modules")
async def get_all_modules():
    modules = db_helper.module_operations.get_all_modules()
    return {"modules": modules}

@app.get("/module/{moduleName}")
async def get_module(moduleName: str):
    module = db_helper.module_operations.get_module(moduleName)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    return module

@app.put("/module/{moduleName}")
async def update_module(moduleName: str, module: Module):
    db_helper.module_operations.update_module(moduleName, module)

@app.delete("/module/{moduleName}")
async def delete_module(moduleName: str):
    existing_module = db_helper.get_module(moduleName)
    if not existing_module:
        raise HTTPException(status_code=404, detail="Module not found")

    db_helper.delete_module(moduleName)

    return {"message": "Module deleted successfully"}

'''----------------------------------    Lesson      ---------------------------------- '''
@app.post("/lesson")
async def create_lesson(lesson: Lesson):
    db_helper.lesson_operations.create_lesson(lesson)

    return {"message": "Lesson created successfully"}

@app.get("/lessons")
async def get_all_lessons():
    lessons = db_helper.lesson_operations.get_all_lessons()
    return {"lessons": lessons}

@app.get("/lesson/{lessonName}")
async def get_lesson(lessonName: str):
    lesson = db_helper.lesson_operations.get_lesson(lessonName)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return lesson

@app.put("/lesson/{lessonName}")
async def update_lesson(lessonName: str, lesson: Lesson):
    db_helper.lesson_operations.update_lesson(lessonName, lesson)

@app.delete("/lesson/{lessonName}")
async def delete_lesson(lessonName: str):
    existing_lesson = db_helper.get_lesson(lessonName)
    if not existing_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    db_helper.delete_lesson(lessonName)

    return {"message": "Lesson deleted successfully"}

'''----------------------------------    Question      ---------------------------------- '''

@app.post("/question")
async def create_question(question: Question):
    db_helper.question_operations.create_question(question)

    return {"message": "Question created successfully"}

@app.get("/questions")
async def get_all_questions():

    questions = db_helper.question_operations.get_all_questions()
    return {"questions": questions}

@app.get("/question/{questionName}")
async def get_question(questionName: str):
    question = db_helper.question_operations.get_question(questionName)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question

@app.put("/question/{questionName}")
async def update_question(questionName: str, question: Question):
    db_helper.question_operations.update_question(questionName, question)

@app.delete("/question/{questionName}")
async def delete_question(questionName: str):
    existing_question = db_helper.get_question(questionName)
    if not existing_question:
        raise HTTPException(status_code=404, detail="Question not found")

    db_helper.delete_question(questionName)

    return {"message": "Question deleted successfully"}

'''----------------------------------    Submission      ---------------------------------- '''

@app.post("/submission")
async def create_submission(submission: Submission):
    db_helper.submission_operations.create_submission(submission)

    return {"message": "Submission created successfully"}


@app.get("/submissions")
async def get_all_submissions():
    submissions = db_helper.submission_operations.get_all_submissions()
    return {"submissions": submissions}

@app.get("/submission/{submissionName}")
async def get_submission(submissionName: str):
    submission = db_helper.submission_operations.get_submission(submissionName)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    return submission

@app.put("/submission/{submissionName}")
async def update_submission(submissionName: str, submission: Submission):
    db_helper.submission_operations.update_submission(submissionName, submission)


@app.delete("/submission/{submissionName}")
async def delete_submission(submissionName: str):
    existing_submission = db_helper.get_submission(submissionName)
    if not existing_submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    db_helper.delete_submission(submissionName)

    return {"message": "Submission deleted successfully"}

'''----------------------------------    Test Case      ---------------------------------- '''

@app.post("/testcase")
async def create_testcase(testcase: testCase):
    db_helper.testcase_operations.create_testcase(testcase)

    return {"message": "Test Case created successfully"}