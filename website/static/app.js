$(document).ready(function() {
    // Listen for click events on the "Delete" buttons
    $('.delete-college').click(function(event) {
        event.preventDefault();
        var collegeCode = $(this).data('college-code');

        if (confirm('Are you sure you want to delete this college?')) {
            // Send a DELETE request using AJAX
            $.ajax({
                type: 'DELETE',
                url: '/colleges/delete/' + collegeCode,
                success: function(data) {
                    if (data.success) {
                        // Remove the deleted row from the table
                        $(event.target).closest('tr').remove();
                        alert('College deleted successfully.');
                    } else {
                        alert('Failed to delete the college.');
                    }
                },
                error: function() {
                    alert('Failed to delete the college.');
                }
            });
        }
    });

    // Listen for the "Edit" button click for colleges
    const editButtonsCollege = document.querySelectorAll('.edit-college');
    editButtonsCollege.forEach(button => {
        button.addEventListener('click', () => {
            const collegeCode = button.getAttribute('data-college-code');
            const collegeName = button.getAttribute('data-college-name');

            // Populate the edit form fields
            const editCollegeCodeField = document.getElementById('editCollegeCode');
            const editCollegeNameField = document.getElementById('editCollegeName');
            editCollegeCodeField.value = collegeCode;
            editCollegeNameField.value = collegeName;
        });
    });

    // Listen for the "Edit" button click for courses
    const editButtonsCourse = document.querySelectorAll('.edit-course');
    editButtonsCourse.forEach(button => {
        button.addEventListener('click', () => {
            const courseCode = button.getAttribute('data-course-code');
            const courseName = button.getAttribute('data-course-name');
            const collegeCode = button.getAttribute('data-college-code');

            // Populate the edit form fields
            const editCourseCodeField = document.getElementById('editCourseCode');
            const editCourseNameField = document.getElementById('editCourseName');
            const editCollegeCodeField = document.getElementById('editCollegeCode');
            editCourseCodeField.value = courseCode;
            editCourseNameField.value = courseName;
            editCollegeCodeField.value = collegeCode;
        });
    });

    // Edit college submission
    $(".edit-college").click(function () {
        var collegeCode = $(this).data("college-code");
        var collegeName = $(this).data("college-name");

        $("#editCollegeCode").val(collegeCode);
        $("#editCollegeName").val(collegeName);
    });

    $("#editCollegeForm").submit(function (e) {
        e.preventDefault();
        var collegeCode = $("#editCollegeCode").val();
        var newCollegeName = $("#editCollegeName").val();

        $.ajax({
            type: "POST",
            url: `/colleges/edit/${collegeCode}`,
            data: {
                collegeName: newCollegeName,
            },
            success: function (response) {
                if (response.success) {
                    alert("College updated successfully");
                    window.location.reload();
                } else {
                    alert("Failed to update college");
                }
            },
        });
    });

    // Edit course submission
    $(".edit-course").click(function () {
        var courseCode = $(this).data("course-code");
        var courseName = $(this).data("course-name");
        var collegeCode = $(this).data("college-code");

        $("#editCourseCode").val(courseCode);
        $("#editCourseName").val(courseName);
        $("#editCollegeCode").val(collegeCode); // Optionally, you can populate the college code field
    });

    $("#editCourseForm").submit(function (e) {
        e.preventDefault();
        var courseCode = $("#editCourseCode").val();
        var newCourseName = $("#editCourseName").val();
        var collegeCode = $("#editCollegeCode").val(); // Add an input field for college code in your edit form

        $.ajax({
            type: "POST",
            url: `/courses/edit/${courseCode}`,
            data: {
                courseName: newCourseName,
                collegeCode: collegeCode, // Include college code in the data
            },
            success: function (response) {
                if (response.success) {
                    alert("Course updated successfully");
                    window.location.reload();
                } else {
                    alert("Failed to update course");
                }
            },
        });
    });
});
