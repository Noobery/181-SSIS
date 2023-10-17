from website import mysql

class CourseModel:
    @classmethod
    def create_course(cls, name, code, college_code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO course (code, name, college_code) VALUES (%s, %s, %s)", (code, name, college_code))
            mysql.connection.commit()
            return "Course created successfully"
        except Exception as e:
            return f"Failed to create course: {str(e)}"
    @classmethod
    def get_courses(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT course.code AS course_code, course.name AS course_name, college.code AS college_code, college.name AS college_name FROM course INNER JOIN college ON course.college_code = college.code")
        courses = cur.fetchall()
        return courses
