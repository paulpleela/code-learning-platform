from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict
import os, sys
from ZODB import FileStorage, DB

from databaseHelper.database import ZODBHelper

app = FastAPI()

db_helper = ZODBHelper('mydatabase.fs')

class StudentRegister(BaseModel):
    username: str
    password: str
    email: str

class StudentLogin(BaseModel):
    username: str
    password: str

@app.post("/register/")
async def register_student(student: StudentRegister):
    existing_student = db_helper.get_student(student.username)
    if existing_student:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add student to the database
    db_helper.add_student(student.username, student.dict())

    return {"message": "Student registered successfully"}

@app.post("/login/")
async def login_student(student: StudentLogin):
    existing_student = db_helper.get_student(student.username)
    if not existing_student or existing_student["password"] != student.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": student.username}
