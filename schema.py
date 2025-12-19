from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    id:int
    name:str
    percentage:float 