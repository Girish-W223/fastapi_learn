from fastapi import FastAPI,HTTPException
from schema import Student
app=FastAPI()

Students=[
    Student(id=2,name="abc",percentage=82.5),
    Student(id=3,name="xyz",percentage=50),
    Student(id=1,name="pqr",percentage=60.99)
]

@app.get('/student')
def get_all():
    return Students 

@app.post('/student')
def add_student(stud:Student):
        Students.append(stud)
        return {"addition successful"}
    
@app.get('/student/{id}')
def get_one(id:int):
    for stud in Students:
        if stud.id==id:
            return stud  
    return{"student not found"}




@app.delete('/student/{id}')
def delete(id:int):
    for i,stud in enumerate(Students):
          if stud.id==id:
               Students.pop(i)
               return{"message:deleted successfully"}
    return{"message: student not found "}



@app.put('/student/{id}')
def update(id:int,u_stud:Student):
    for i,stud in enumerate(Students):
        if stud.id==id:
            Students[i]=u_stud 
            return{"message":"student updated"}
    return{"message: student not found "}
