import datetime
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict
import os, sys
from ZODB import FileStorage, DB

app = FastAPI()

from database import CourseCodeGenerator, ZODBHelper, Student
code_generator = CourseCodeGenerator()
db_helper = ZODBHelper('mydatabase.fs')
 
 # Base model for student registration, login, and course creation

class StudentRegister(BaseModel):
    username: str
    password: str
    

class StudentLogin(BaseModel):
    username: str
    password: str

class Course(BaseModel):
    name: str
    description: Optional[str]
    teacherName: str
    created_date: datetime = datetime.now()



@app.post("/register/")
async def register_student(student: StudentRegister):
    existing_student = db_helper.get_student(student.username)
    if existing_student:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add student to the database
    
    student = Student(student.username, student.password, "student", [],)
    db_helper.add_student(student.username, student.dict())

    return {"message": "Student registered successfully"}

@app.post("/login/")
async def login_student(student: StudentLogin):
    existing_student = db_helper.get_student(student.username)
    if not existing_student or existing_student["password"] != student.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": student.username}


@app.post("/course")
async def course(course: Course):
    existing_course = db_helper.get_course(course.name)
    if existing_course:
        raise HTTPException(status_code=400, detail="Course already exists")

    # Add course to the database
    # courseName, courseCreatedDate, courseCode, courseTeacherName, studentList, moduleList, quizzList
    course = Course(course.name, course.created_date, course.teacherName, [], [], [])
    db_helper.add_course(course.name, course.dict())

    return {"message": "Course created successfully"}

@app.post("/logout/")
async def logout_student():
    return {"message": "Logout successful"}

@app.post("/createCourse/")
async def create_course():
    
    return {"message": "Course created successfully"}