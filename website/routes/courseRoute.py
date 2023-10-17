from flask import Blueprint, render_template, request, redirect, url_for
from website.models.courseModels import CourseModel
from website.models.collegeModels import CollegeModel

courseRoute = Blueprint('courses', __name__)
course_model = CourseModel()
college_model = CollegeModel()

@courseRoute.route("/courses", methods=["GET", "POST"])
def courses():
    if request.method == "POST":
        name = request.form.get("courseName")
        code = request.form.get("courseCode")
        college_code = request.form.get("collegeCode")
        course_model.create_course(name, code, college_code)

    courses = course_model.get_courses()
    colleges = college_model.get_colleges()
    return render_template("courses.html", courses=courses, colleges=colleges)
