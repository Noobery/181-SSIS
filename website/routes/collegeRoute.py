from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from website.models.collegeModels import CollegeModel

collegeRoute = Blueprint('college', __name__)
college_model = CollegeModel()

@collegeRoute.route("/colleges", methods=["GET", "POST"])
def colleges():
    if request.method == "POST":
        name = request.form.get("collegeName")
        code = request.form.get("collegeCode")
        college_model.create_college(name, code)

    colleges = college_model.get_colleges()
    return render_template("colleges.html", colleges=colleges)

@collegeRoute.route("/colleges/delete/<string:college_code>", methods=["DELETE"])
def delete_college(college_code):
    result = college_model.delete_college(college_code)
    return jsonify({'success': result == 'College deleted successfully'})

@collegeRoute.route("/colleges/edit/<string:college_code>", methods=["POST"])
def edit_college(college_code):
    new_name = request.form.get("collegeName")
    result = college_model.update_college(college_code, new_name)
    return jsonify({'success': result == 'College updated successfully'})

