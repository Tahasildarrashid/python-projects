from fastapi import *
from pydantic import *
from starlette import * 
app = FastAPI()

class StudentList:
    name: str
    age: int 
    college: str
    cgpa: int

    def __init__(self, name, age, college, cgpa):
        self.name = name
        self.age = age
        self.college = college
        self.cgpa = cgpa

class StudentListDef(BaseModel):
    name: str = Field(description="Enter your name",max_length=20)
    age: int = Field(ge=18, le=24)
    college: str = Field(description="By default college name is given", default="PES UNIVERSITY")
    cgpa: int = Field(description="Enter the number upto 2 decimals")

    model_config = {
        "json_extra_schema" : {
            "example": {
                "name": "JOHN",
                "age": 22,
                "college": "PES UNIVERSITY RR Campus",
                "cgpa": 8.13
            }
        }
    }

studentsList = [
    {'name': 'rashid', 'age': 22, 'college': 'PES UNIVERSITY EC CAMPUS', 'cgpa': 8.13},
    {'name': 'vruddhi', 'age': 22, 'college': 'PES UNIVERSITY RR CAMPUS', 'cgpa': 9.00},
    {'name': 'rajeev kalose', 'age': 22, 'college': 'PES UNIVERSITY EC CAMPUS', 'cgpa': 8.46},
    {'name': 'rohit', 'age': 22, 'college': 'PES UNIVERSITY EC CAMPUS', 'cgpa': 8.89},
    {'name': 'pratham shetty', 'age': 22, 'college': 'PES UNIVERSITY RR CAMPUS', 'cgpa': 8.75},
]

@app.get('/students', status_code=status.HTTP_200_OK)
def get_all_students_list():
    return studentsList

# path parameters validation 
# request parameters
@app.get('/studentsInfo/{name}')
def get_specific_student_info(name: str = Path(min_length=4)):
    for student in studentsList:
        if student.get('name').casefold() == name.casefold():
            return student
        
    raise HTTPException(404, detail="Student Not Found")
        
# Query parameters
@app.get('/students/')
def get_students_by_college(college: str = Query(min_length=15, max_length=25)):
    result = []
    for student in studentsList:
        if student.get("college").casefold() == college.casefold():
            result.append(student)

    return result
            
@app.post('/addStudent')
def add_a_student(student: StudentListDef):
    new_student = StudentList(**student.model_dump())
    studentsList.append(new_student)

@app.put('/update')
def update_a_student(student_detail=Body()):
    for i in range(len(studentsList)):
        if studentsList[i].get('name').casefold() == student_detail.get('name').casefold():
            studentsList[i] = student_detail

@app.delete('/delete')
def delete_a_student(name: str):
    for student in range(len(studentsList)):
        if studentsList[student].get('name').casefold() == name.casefold():
            studentsList.pop(student)
            
    raise HTTPException(status=404, detail="Student Not Found")