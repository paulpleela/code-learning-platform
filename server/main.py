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

class StudentRegister(BaseModel):
    username: str
    password: str
    role: str
    
class StudentLogin(BaseModel):
    username: str
    password: str
    role: str

class TeacherRegister(BaseModel):
    username: str
    password: str
    role: str
    
class TeacherLogin(BaseModel):
    username: str
    password: str
    role: str

class CourseCreated(BaseModel):
    courseName: str
    teacherName: str
    

@app.post("/api/student/register")
async def register_student(student: StudentRegister):
    existing_student = db_helper.get_student(student.username)
    if existing_student:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add student to the database
    
    student = Student(student.username, student.password, "student", [],)
    db_helper.add_student(student.username, student.dict())

    return {"message": "Student registered successfully"}

@app.post("api/student/login")
async def login_student(student: StudentLogin):
    existing_student = db_helper.get_student(student.username)
    if not existing_student or existing_student["password"] != student.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": student.username}

@app.post("/api/teacher/register")
async def register_teacher(teacher: TeacherRegister):
    existing_teacher = db_helper.get_teacher(teacher.username)
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add teacher to the database
    teacher = Teacher(teacher.username, teacher.password, "teacher", [])
    db_helper.add_teacher(teacher.username, teacher.dict())

    return {"message": "Teacher registered successfully"}

@app.post("api/teacher/login")
async def login_teacher(teacher: TeacherLogin):
    existing_teacher = db_helper.get_teacher(teacher.username)
    if not existing_teacher or existing_teacher["password"] != teacher.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": teacher.username}

'''----------------------------------    Course      ---------------------------------- '''
@app.post("api/teacher/course")
async def course(course: CourseCreated):
    
    # Use teacherName to search for the teacher in the database
    # check if the course exists in a teacher's ownedCourseList
    existing_course = db_helper.get_course(course.courseName, course.teacherName)
    if existing_course:
        raise HTTPException(status_code=400, detail="Course already exists in the teacher's ownedCourseList")

    # Add course to the database
    # courseName, courseCreatedDate, courseCode, courseTeacherName, studentList, moduleList, quizzList
    createdDate = datetime.datetime.now()
    courseCode = code_generator.generate_course_code()
    print("Course code: ", courseCode)
    newCourse = Course(courseName=course.name, courseCreatedDate=createdDate, courseCode=courseCode, courseTeacherName=course.teacherName, 
                       studentList=[], moduleList=[], quizzList=[])

    db_helper.add_course(course.name, newCourse)
    newCourse.print_details()
        
    return {"message": "Course created successfully"}

@app.get("/course/{courseName}")
async def get_course(courseName: str):
    existing_course = db_helper.get_course(courseName)
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return existing_course

@app.put("/course/{courseName}")
async def update_course(courseName: str, course: CourseCreated):
    existing_course = db_helper.get_course(courseName)
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Update the course
    existing_course["name"] = course.name
    existing_course["teacherName"] = course.teacherName

    db_helper.update_course(courseName, existing_course)

    return {"message": "Course updated successfully"}

@app.delete("/course/{courseName}")
async def delete_course(courseName: str):
    existing_course = db_helper.get_course(courseName)
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    db_helper.delete_course(courseName)

    return {"message": "Course deleted successfully"}

@app.post("/logout/")
async def logout_student():
    return {"message": "Logout successful"}

@app.post("/createCourse/")
async def create_course():
    
    return {"message": "Course created successfully"}