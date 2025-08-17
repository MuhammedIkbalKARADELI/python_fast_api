import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
import time

from app.config import POSTGRES_CONN_INFO_LOCAL



def get_db_connection():

    while True:
        try:
            conn = psycopg2.connect(POSTGRES_CONN_INFO_LOCAL)
            cursor = conn.cursor()
            print("Connection is Successful!")
            break
        except Exception as error:
            print("Connection Failed!")
            print("Error", error)
            time.sleep(2)
    return conn, cursor


def create_students_db():

    conn, cursor = get_db_connection()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL);
                    """
        )
        conn.commit()
        cursor.close()
        print("rag_log_queries database was checked")
    except Exception as e:
        print(f"There is an issue for creating db error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_students_db()
