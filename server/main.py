import datetime
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from pydantic import BaseModel
from typing import Optional, Dict
import os, sys
from ZODB import FileStorage, DB

from fastapi import FastAPI, Request
app = FastAPI()


from database import *

courseCode_generator = CodeGenerator()
fileCodeGenerator = CodeGenerator()

db_helper = ZODBHelper('mydatabase.fs')
 
 # Base model for student registration, login, and course creation

class UserRegister(BaseModel):
    username: str
    name: str
    password: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str


class CourseCreated(BaseModel):
    name: str
    teacherName: str

class ModuleModel(BaseModel):
    name: str
    lessonList: list
    questionsList: list
    dueDate: datetime.datetime
    status: str

class LessonModel(BaseModel):
    name: str

class QuizzModel(BaseModel):
    name: str
    content: str
    answer: str


class SubmissionModel(BaseModel):
    name: str
    content: str
    answer: str

class testCaseModel(BaseModel):
    name: str
    input: str
    output: str

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

    return {"message": "Login successful", "username": user.username, "role": user.role}

@app.get("/api/student/course_list")
async def get_course_list(username: str):
    courses = db_helper.course_operations.get_student_course_list(username)
    return {"course_names": courses}

@app.get("/api/teacher/course_list")
async def get_course_list(username: str):
    courses = db_helper.course_operations.get_teacher_course_list(username)
    return {"course_names": courses}



'''----------------------------------    Course      ---------------------------------- 
    '''
@app.post("/api/teacher/course")
async def course(courseCreated: CourseCreated):
    course_code = courseCode_generator.generate_code()
    course_created_date = datetime.datetime.now()
    course = Course(courseCreated.name, course_created_date, course_code, courseCreated.teacherName, [], [], [])

    success = db_helper.course_operations.create_course(course, course.courseTeacherName)
        
    return {"success": success}

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

@app.get("/api/teacher/ownedCourses/{teacherName}")
async def get_owned_courses(teacherName: str):
    ownedCourses = db_helper.course_operations.get_courses_by_teacherName(teacherName)
    return {"courses": ownedCourses}

@app.post("/api/enroll")
async def enroll_course(courseCode: str, username: str):
    success = db_helper.course_operations.enroll_course(courseCode, username)
    return {"success": success}


# update operation 
@app.put("/course/rename/{courseCode}/{newName}")
async def update_course(courseCode: str, newName: str):
    db_helper.course_operations.rename_course(courseCode, newName)

@app.delete("/course/{courseCode}/{username}")
async def delete_course(courseCode: str, username: str):
    success = False
    existing_course = db_helper.course_operations.get_course_by_code(courseCode)
    # if not existing_course:
    #     raise HTTPException(status_code=404, detail="Course not found")

    success = db_helper.course_operations.delete_course_ByCourseCode(courseCode, username)

    return {"success": success}

'''----------------------------------    Module      ---------------------------------- '''
@app.post("/module")
async def create_module(module: ModuleModel):
    db_helper.module_operations.create_module(module)



    return {"message": "Module created successfully"}

@app.get("/modules/{courseCode}")
async def get_all_modules(courseCode: str):
    modules = db_helper.module_operations.get_all_modules(courseCode)
    return {"modules": modules}

@app.get("/module/{courseCode}/{moduleIndex}")
async def get_moduleByIndex(courseCode: str, moduleIndex: str):
    module = db_helper.module_operations.get_module(courseCode, moduleIndex)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    return module

@app.put("/module/{moduleName}")
async def update_module(moduleName: str, module: ModuleModel):
    db_helper.module_operations.update_module(moduleName, module)

@app.delete("/module/{moduleName}")
async def delete_module(moduleName: str):
    existing_module = db_helper.get_module(moduleName)
    if not existing_module:
        raise HTTPException(status_code=404, detail="Module not found")

    db_helper.delete_module(moduleName)

    return {"message": "Module deleted successfully"}

'''----------------------------------    Lesson      ---------------------------------- '''
@app.post("/lesson/{courseCode}/{moduleIndex}/{lessonName}")
async def create_lesson(courseCode: str, moduleIndex: str, lessonName: str, file: UploadFile = File(None)):

    if file is None:
        return {"error": "No file provided"}

    if file.content_type == "application/pdf":
        file_extension = ".pdf"
    elif file.content_type == "video/mp4":
        file_extension = ".mp4"
    else:
        return {"error": "Unsupported file type"}

    lessonCode = CodeGenerator.generate_course_code(prefix="L", length=8)
    # Generate a unique filename
    file_name = f"{lessonCode}{file_extension}"

    # Create the directory if it doesn't exist
    UPLOAD_DIRECTORY = "static"
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    # Save the file to the "static" directory
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Optionally, you can save the file information to a database
    # For example:
    lessonObject = Lesson(lessonName, file_path)
    db_helper.lesson_operations.create_lesson(courseCode, moduleIndex, lessonObject)

    return {"message": "Lesson created successfully", "file_path": file_path}

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
async def update_lesson(lessonName: str, lesson: LessonModel):
    db_helper.lesson_operations.update_lesson(lessonName, lesson)

@app.delete("/lesson/{lessonName}")
async def delete_lesson(lessonName: str):
    existing_lesson = db_helper.get_lesson(lessonName)
    if not existing_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    db_helper.delete_lesson(lessonName)

    return {"message": "Lesson deleted successfully"}

'''----------------------------------    Quizz      ---------------------------------- '''

@app.post("/quizz")
async def create_qizz(Quizz: QuizzModel):
    db_helper.question_operations.create_question(Quizz)

    return {"message": "Question created successfully"}

@app.get("/quizzs")
async def get_all_questions():

    quizzList = db_helper.quizz_operations.get_all_quizzs()
    return {"quizzList": quizzList}

@app.get("/quizz/{quizzIndex}")
async def get_quizz_ByIndex(quizzIndex: str):
    quizz = db_helper.quizz_operations.get_quizz_by_index(quizzIndex)
    if not quizz:
        raise HTTPException(status_code=404, detail="Quizz not found")

    return quizz

@app.put("/question/{quizzIndex}")
async def update_question(quizzIndex: str, quiz: QuizzModel):
    db_helper.quizz_operations.update_quizz(quizzIndex, quiz)


@app.delete("/question/{quizzIndex}")
async def delete_question(quizzIndex: str):
    
    existing_quizz = db_helper.quizz_operations.get_quizz_by_index(quizzIndex)
    if not existing_quizz:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db_helper.quizz_operations.delete_quizz(quizzIndex)

    return {"message": "Question deleted successfully"}

'''----------------------------------    Submission      ---------------------------------- '''

@app.post("/submission")
async def create_submission(submission: SubmissionModel):
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
async def update_submission(submissionName: str, submission: SubmissionModel):
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
async def create_testcase(testcase: testCaseModel):
    db_helper.testcase_operations.create_testcase(testcase)

    return {"message": "Test Case created successfully"}