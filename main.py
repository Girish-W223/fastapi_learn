from fastapi import FastAPI,HTTPException
from schema import Student
app=FastAPI()

Students=[
    Student(id=2,name="abc",percentage=82.5),
    Student(id=3,name="xyz",percentage=50),
    Student(id=1,name="pqr",percentage=60.99)
]

@app.get('/')
def get_all():
    return Students 

@app.post('/')
def add_student(stud:Student):
        Students.append(stud)
        return {"addition successful"}
    
    
    