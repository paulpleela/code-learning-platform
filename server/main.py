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
    

@app.post("/api/user/register")
async def register_user(user: UserRegister):
    existing_user = db_helper.get_student(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add student to the database
    if (user.role == "student"):
        student = Student(user.username, user.password, user.role, [],)
        db_helper.add_student(student.username, student)
    
    if (user.role == "teacher"):
        teacher = Teacher(user.username, user.password, user.role, [])
        db_helper.add_teacher(teacher.username, teacher)

    return {"message": "user registered successfully"}

@app.post("/api/user/login")
async def login_student(student: UserLogin):
    existing_student = db_helper.get_student(student.username)  # object
    # self.root.students[str(student_name): student obj]
    print("existing_student", existing_student)
    if not existing_student or existing_student.password != student.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": existing_student.username}

'''----------------------------------    Course      ---------------------------------- 
    '''
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

    db_helper.create_courseBy_teacher(courseCode, newCourse)
    newCourse.print_details()
        
    return {"message": "Course created successfully"}

@app.get("/courses")
async def get_course():
    courses = db_helper.get_courses()
    return {"courses": courses}

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
