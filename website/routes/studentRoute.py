from flask import Blueprint, render_template, request, jsonify, flash
from website.models.studentModels import StudentModel
from website.models.courseModels import CourseModel
from website.models.collegeModels import CollegeModel
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import destroy as cloudinary_destroy
import cloudinary

studentRoute = Blueprint('students', __name__)
student_model = StudentModel()
course_model = CourseModel()
college_model = CollegeModel()

@studentRoute.route("/students", methods=["GET", "POST"])
def students():
    has_prev = False
    has_next = False
    
    if request.method == "POST":
        # Add a new student
        add_student()
    # Handle search query


    search_query = request.args.get("search")
    page_number = request.args.get('page_number', 1, type=int)
    page_size = request.args.get('page_size', 8, type=int)

    courses = course_model.get_courses()
    students = []

    search_query = "" if search_query is None else search_query

    if search_query:
        students = student_model.search_students(search_query)
    else:
        students_data = student_model.get_students(page_number=page_number, page_size=page_size)
        students = students_data.get("results")
        has_prev = students_data.get("has_prev")
        has_next = students_data.get("has_next")

    return render_template(
        "students.html",
        courses=courses,
        students=students,
        search_query=search_query,
        page_number=page_number,
        page_size=page_size,
        has_prev=has_prev,
        has_next=has_next,
    )

def add_student():
    id = request.form.get("studentID")
    firstname = request.form.get("firstName")
    lastname = request.form.get("lastName")
    course_code = request.form.get("courseCode")
    year = request.form.get("year")
    gender = request.form.get("gender")
    student_model.create_student(id, firstname, lastname, course_code, year, gender)
    flash('Student created successfully', 'success')



@studentRoute.route("/students/delete/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
    result = student_model.delete_student(student_id)
    return jsonify({'success': result == 'Student deleted successfully'})

@studentRoute.route("/students/edit/<string:student_id>", methods=["POST"])
def edit_student(student_id):
    new_first_name = request.form.get("firstName")
    new_last_name = request.form.get("lastName")
    new_course_code = request.form.get("courseCode")
    new_year = request.form.get("year")
    new_gender = request.form.get("gender")

    result = student_model.update_student(
        student_id, new_first_name, new_last_name, new_course_code, new_year, new_gender
    )

    return jsonify({'success': result == 'Student updated successfully'})


@studentRoute.route('/update_profile_pic', methods=['POST'])
def update_profile_pic():
    try:
        data = request.get_json()
        student_id = data.get('studentId')
        secure_url = data.get('secureUrl')

        # Delete existing profile picture from Cloudinary
        existing_profile_pic_url = student_model.get_student_profile_pic_url(student_id)
        if existing_profile_pic_url:
            public_id = existing_profile_pic_url.split('/')[-1].split('.')[0]
            deletion_response = cloudinary_destroy(public_id)
            print(deletion_response)
        
        # Update profile picture URL in the database
        result = student_model.update_student_profile_pic(student_id, secure_url)

        return jsonify({'secureUrl': secure_url, 'message': 'Profile picture updated successfully'})

    except Exception as e:
        return jsonify({'error': 'Failed to update profile picture'})