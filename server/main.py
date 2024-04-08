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
    dueDate: str    # date format: "2021 "

class LessonModel(BaseModel):
    name: str


class QuizzModel(BaseModel):
    questionName: str
    questionInstruction: str
    inputVarNameList: list
    testCaseDict: dict
    #submissionDict: Dict
    #which_student_finsished_StatusDict: Dict


class SubmissionModel(BaseModel):
    pythonCode: str
    testCaseResults: list # [fail, none, fail]


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

@app.get("/course/getCourseName/{courseCode}")
async def get_course_name(courseCode: str):
    course = db_helper.course_operations.get_course_by_code(courseCode)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course.Name

@app.get("/api/teacher/ownedCourses/{teacherName}")
async def get_owned_courses(teacherName: str):
    ownedCourses = db_helper.course_operations.get_courses_by_teacherName(teacherName)
    return {"courses": ownedCourses}

@app.post("/api/enroll")
async def enroll_course(courseCode: str, username: str):
    success = db_helper.course_operations.enroll_course(courseCode, username)
    return {"success": success}

@app.post("/api/unenroll")
async def unenroll_course(courseCode: str, username: str):
    success = db_helper.course_operations.unenroll_course(courseCode, username)
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
@app.post("/module/{moduleName}/{courseCode}")
async def create_module(moduleName: str, courseCode: str):

    moduleObject = Module(moduleName, [], [], "", [])
    success = db_helper.module_operations.create_module(moduleObject, courseCode)
    
    return {"success": success}

@app.get("/modules/{courseCode}")
async def get_all_modules(courseCode: str):
    modules = db_helper.module_operations.get_all_modules(courseCode)
    return {"modules": modules}

@app.get("/modules/moduleNamesList/{courseCode}")
async def get_all_modulesNames(courseCode: str):
    modules = db_helper.module_operations.get_all_modules(courseCode)

    # create module name list from modules object list
    moduleNames = []
    for module in modules:
        moduleNames.append(module["name"])
    
    return {"moduleNames": moduleNames}


@app.get("/module/{courseCode}/{moduleIndex}")
async def get_moduleByIndex(courseCode: str, moduleIndex: str):
    module = db_helper.module_operations.getModule_ByIndex(courseCode, moduleIndex)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    return module

@app.put("/module/{courseCode}/{moduleIndex}")
async def update_module_byIndex(courseCode: str, moduleIndex: str, moduleModel: ModuleModel):
    
    success = db_helper.module_operations.update_module(courseCode, moduleIndex, moduleModel)
    return {"success": success}

@app.delete("/module/{courseCode}/{moduleIndex}")
async def delete_module(courseCode:str, moduleIndex: str):
    existing_module = db_helper.module_operations.getModule_ByIndex(courseCode, moduleIndex)
    if not existing_module:
        raise HTTPException(status_code=404, detail="Module not found")

    db_helper.module_operations.delete_module(courseCode, moduleIndex)

    return {"message": "Module deleted successfully"}

'''----------------------------------    Lesson      ---------------------------------- '''
@app.post("/lesson/{courseCode}/{moduleIndex}/{lessonName}/{file_type}")
async def create_lesson(courseCode: str, moduleIndex: str, lessonName: str, file_type: str, file: UploadFile = File(None)):    
    lessonCode = fileCodeGenerator.generate_code(prefix="L", length=8)
    # Generate a unique filename
    file_name = f"{lessonCode}{file_type}"

    print("Everything", courseCode, moduleIndex, lessonName, file_name)
    # Create the directory if it doesn't exist
    UPLOAD_DIRECTORY = "static"
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    # Save the file to the "static" directory
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    print("file path", file_path)
    # Optionally, you can save the file information to a database
    # For example:

    lessonObject = Lesson(lessonName, file_name)
    print("create lesson api", courseCode)
    success = db_helper.lesson_operations.create_lesson(courseCode, moduleIndex, lessonObject)

    return {"success": success}

@app.get("/lessons/{courseCode}/{moduleIndex}")
async def get_all_lessons(courseCode: str, moduleIndex: str):
    lessons = db_helper.lesson_operations.get_all_lessons(courseCode, moduleIndex)
    return {"lessons": lessons}

@app.get("/lesson/lessonNamesList/{courseCode}/{moduleIndex}")
async def get_all_lessonNames(courseCode: str, moduleIndex: str):
    lessons = db_helper.lesson_operations.get_all_lessons(courseCode, moduleIndex)

    # create lesson name list from lessons object list
    lessonNames = []
    for lesson in lessons:
        lessonNames.append(lesson["name"])
    
    return {"lessonNames": lessonNames}

@app.get("/lesson/{courseCode}/{moduleIndex}/{lessonIndex}")
async def get_lesson_ByIndex(courseCode: str, moduleIndex: str, lessonIndex: str):
    lesson = db_helper.lesson_operations.get_lesson_ByIndex(courseCode, moduleIndex, lessonIndex)
    print("lesson file path", lesson)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return lesson

@app.put("/lesson/{courseCode}/{moduleIndex}/{lessonIndex}")
async def update_lesson(courseCode: str, moduleIndex: str, lessonIndex: str, lesson: LessonModel):
    db_helper.lesson_operations.update_lesson_ByIndex(courseCode, moduleIndex, lessonIndex, lesson)

@app.delete("/lesson/{courseCode}/{moduleIndex}/{lessonIndex}")
async def delete_lesson(courseCode: str, moduleIndex: str, lessonIndex: str):
    existing_lesson = db_helper.lesson_operations.get_lesson_ByIndex(courseCode, moduleIndex, lessonIndex)
    if not existing_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    db_helper.lesson_operations.delete_lesson_ByIndex(courseCode, moduleIndex, lessonIndex)

    return {"message": "Lesson deleted successfully"}

'''----------------------------------    Quizz      ---------------------------------- '''
@app.post("/quizz/{courseCode}/{moduleIndex}")
async def create_quizz(courseCode: str, moduleIndex: str, quizz: QuizzModel):
    
    quizzObject = Quiz(quizz.questionName, quizz.questionInstruction, quizz.inputVarNameList, quizz.testCaseDict, {}, [])
    success = db_helper.quizz_operations.create_quizz(courseCode, moduleIndex, quizzObject)

    return {"success": success}

@app.get("/quizzes/{courseCode}/{moduleIndex}")
async def get_all_quizzes(courseCode: str, moduleIndex: str):
    quizzes = db_helper.quizz_operations.get_all_quizzs(courseCode, moduleIndex)
    return {"quizzes": quizzes}

@app.get("/quizzes/quizNamesList/{courseCode}/{moduleIndex}")
async def get_all_quizzNames(courseCode: str, moduleIndex: str):
    quizzes = db_helper.quizz_operations.get_all_quizzs(courseCode, moduleIndex)

    # create quizz name list from quizz object list
    quizzNames = []
    for quizz in quizzes:
        quizzNames.append(quizz["name"])
    
    return {"quizzNames": quizzNames}

@app.get("/quizz/{courseCode}/{moduleIndex}/{quizzIndex}")
async def get_quizz_ByIndex(courseCode: str, moduleIndex: str, quizzIndex: str):
    quizz = db_helper.quizz_operations.get_quizz_ByIndex(courseCode, moduleIndex, quizzIndex)
    if not quizz:
        raise HTTPException(status_code=404, detail="Quizz not found")

    return quizz

@app.put("/quizz/{courseCode}/{moduleIndex}/{quizzIndex}")
async def update_quizz(courseCode: str, moduleIndex: str,  quizzIndex: str, quizz: QuizzModel):
    quizObject = Quiz(quizz.questionName, quizz.questionInstruction, quizz.inputVarNameList, quizz.testCaseDict, {}, [])
    db_helper.quizz_operations.update_quizz_ByIndex(courseCode, moduleIndex, quizzIndex, quizObject)

@app.delete("/quizz/{courseCode}/{moduleIndex}/{quizzIndex}")
async def delete_quizz(courseCode: str, moduleIndex: str, quizzIndex: str):
    existing_quizz = db_helper.quizz_operations.get_quizz_ByIndex(courseCode, moduleIndex, quizzIndex)
    if not existing_quizz:
        raise HTTPException(status_code=404, detail="Quizz not found")

    success = db_helper.quizz_operations.delete_quizz_ByIndex(courseCode, moduleIndex, quizzIndex)
    if success:
        return {"message": "Quizz deleted successfully"}


'''----------------------------------    Submission      ---------------------------------- '''

@app.post("/submission/{courseCode}/{moduleIndex}/{quizzIndex}/{userName}")
async def create_submission(courseCode: str, moduleIndex: str, quizzIndex: str, userName: str, submissionModel: SubmissionModel):

    submission = Submission(submissionModel.pythonCode, submissionModel.testCaseResults)

    
    success = db_helper.submission_operations.create_submission(courseCode, moduleIndex, quizzIndex, userName, submission)

    return {"success": success}

@app.get("/submissions/{courseCode}/{moduleIndex}/{quizzIndex}/{userName}")
async def get_all_submissions(courseCode: str, moduleIndex: str, quizzIndex: str, userName: str):
    submissions = db_helper.submission_operations.get_submission_ByUserName(courseCode, moduleIndex, quizzIndex, userName)
    return {"submissions": submissions}

'''----------------------------------    Certification      ---------------------------------- '''

@app.get("/certifications/{userName}")
async def get_certifications_byUserName(userName: str):
    certifications = db_helper.certification_operations.get_certification_by_userName(userName)
    return {"certifications": certifications}

'''----------------------------------    Calendar      ---------------------------------- '''
@app.get("/calendar/{userName}")
async def get_calendar_byUserName(userName: str):
    calendar = db_helper.calendar_operations.return_calendar_by_userName(userName)

    return {"calendar": calendar}

'''----------------------------------    Dashboard      ---------------------------------- '''
@app.get("/dashboard/student/{userName}")
async def get_dashboard_by_studentUserName(userName: str):
    dashboard = db_helper.dashboard_operations.get_dashboard_by_studentUserName(userName)
   
    return {"dashboard": dashboard}

@app.get("/dashboard/teacher/{userName}")
async def get_dashboard_by_teacherUserName(userName: str):
    dashboard = db_helper.dashboard_operations.get_dashboard_by_teacherUserName(userName)

    return {"dashboard": dashboard}

@app.get("/dashboard/checkUser/{userName}")
async def check_user(userName: str):
    if db_helper.dashboard_operations.checkIfUserIsStudent(userName):
        return {"role": "student"}

    elif db_helper.dashboard_operations.checkIfUserIsTeacher(userName):
        return {"role": "teacher"}
    return {"role": "none"}