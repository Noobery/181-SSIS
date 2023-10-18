from flask import Blueprint, render_template, request, jsonify
from website.models.studentModels import StudentModel
from website.models.courseModels import CourseModel  # You need to import CourseModel
from website.models.collegeModels import CollegeModel

studentRoute = Blueprint('students', __name__)
student_model = StudentModel()
course_model = CourseModel()  # Initialize CourseModel
college_model = CollegeModel()

@studentRoute.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        id = request.form.get("studentID")
        firstname = request.form.get("firstName")
        lastname = request.form.get("lastName")
        course_code = request.form.get("courseCode")
        year = request.form.get("year")
        gender = request.form.get("gender")
        student_model.create_student(id, firstname, lastname, course_code, year, gender)

    students = student_model.get_students()
    courses = course_model.get_courses()
    colleges = college_model.get_colleges()
    return render_template("students.html", students=students, courses=courses, colleges=colleges)
