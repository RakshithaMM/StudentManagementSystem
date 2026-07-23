from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_student():
    return render_template("add_student.html")


@app.route("/students")
def students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    student_list = cursor.fetchall()

    connection.close()

    return render_template("students.html", students=student_list)


@app.route("/save", methods=["POST"])
def save():

    name = request.form["name"]
    email = request.form["email"]

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students(name,email) VALUES(?,?)",
        (name, email)
    )

    connection.commit()

    connection.close()

    return redirect(url_for("students"))

@app.route("/update/<int:id>")
def update(id):

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))

    student = cursor.fetchone()

    connection.close()

    return render_template("update_student.html", student=student)


@app.route("/update_student/<int:id>", methods=["POST"])
def update_student(id):

    name = request.form["name"]
    email = request.form["email"]

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET name=?, email=? WHERE id=?",
        (name, email, id)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("students"))

@app.route("/delete/<int:id>")
def delete_student(id):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    connection.commit()

    connection.close()

    return redirect(url_for("students"))



if __name__ == "__main__":
    app.run(debug=True)