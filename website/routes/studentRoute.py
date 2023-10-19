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

@studentRoute.route("/students/delete/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
    result = student_model.delete_student(student_id)  # Implement the delete_student method in your StudentModel
    return jsonify({'success': result == 'Student deleted successfully'})

@studentRoute.route("/students/edit/<string:student_id>", methods=["POST"])
def edit_student(student_id):
    new_first_name = request.form.get("firstName")
    new_last_name = request.form.get("lastName")
    new_course_code = request.form.get("courseCode")
    new_year = request.form.get("year")
    new_gender = request.form.get("gender")
    
    print (new_first_name, new_last_name, new_course_code, new_year, new_gender, student_id)
    result = student_model.update_student(student_id, new_first_name, new_last_name, new_course_code, new_year, new_gender)
    
    return jsonify({'success': result == 'Student updated successfully'})

