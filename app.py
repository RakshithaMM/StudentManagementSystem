from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="studentdb",
        user="postgres",
        password="postgres"
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_student():
    return render_template("add_student.html")


@app.route("/students")
def students():

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    student_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("students.html", students=student_list)


@app.route("/save", methods=["POST"])
def save():

    name = request.form["name"]
    email = request.form["email"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("students"))


@app.route("/update/<int:id>")
def update(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = %s",
        (id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("update_student.html", student=student)


@app.route("/update_student/<int:id>", methods=["POST"])
def update_student(id):

    name = request.form["name"]
    email = request.form["email"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET name = %s, email = %s WHERE id = %s",
        (name, email, id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("students"))


@app.route("/delete/<int:id>")
def delete_student(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("students"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)