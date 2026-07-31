import psycopg2
import time

connection = None

while connection is None:
    try:
        connection = psycopg2.connect(
            host="db",
            database="studentdb",
            user="postgres",
            password="postgres"
        )
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
)
""")

connection.commit()

cursor.close()
connection.close()

print("PostgreSQL Database Created Successfully!")