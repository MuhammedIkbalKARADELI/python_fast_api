from typing import List, Union
from fastapi import FastAPI
from app.db import get_db_connection
from app.student import Student, StudentCreate
from http.client import HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/status")
async def status():
    return {"Message" : "OK"}


@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    conn, cursor = get_db_connection()
    try:
        cursor.execute(
            """
            INSERT INTO students (first_name, last_name)
            VALUES (%s, %s)
            RETURNING id, first_name, last_name
            """,
            (student.first_name, student.last_name),
        )
        row = cursor.fetchone()  # tuple veya dict olabilir

        # RealDictCursor kullanmıyorsan tuple'ı dict'e çevir
        if isinstance(row, dict):
            data = row
        else:
            colnames = [d[0] for d in cursor.description]
            data = dict(zip(colnames, row))

        conn.commit()
        return data  # response_model=Student bunu doğrular
    except Exception as e:
        try:
            conn.rollback()
        except Exception:
            pass
        # FastAPI HTTPException kwargs kabul eder
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            conn.close()
        except Exception:
            pass


@app.get("/students/", response_model=List[Student])
def get_all_students():
    students = []
    conn, cursor = get_db_connection()
    try:
        cursor.execute("SELECT * FROM Students;")
        rows = cursor.fetchall()
        for row in rows:
           students.append(row) 
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, details=str(e))
    
    conn.close()
    if students:
        return students
    raise HTTPException(status_code=400, details="Student not found!")


@app.get("/student/{student_id}")
def get_one_student(student_id):

    students = []
    conn, cursor = get_db_connection()
    try:
        cursor.execute("SELECT * FROM Students WHERE id = %s;", (student_id))
        rows = cursor.fetchall()
        for row in rows:
           students.append(row) 
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, details=str(e))
    
    conn.close()
    if students:
        return students
    raise HTTPException(status_code=400, details="Student not existed!")


@app.delete("/student/{student_id}")
def delete_student(student_id):
    conn, cursor = get_db_connection()

    try:
        cursor.execute("DELETS FROM Students WHERE id = %s;", (student_id))
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, details=str(e))
    
    conn.close()
    return {"message":"Student deleted succesfully!"}

