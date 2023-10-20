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

    @classmethod
    def update_course(cls, code, new_name, college_code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE course SET name = %s, college_code = %s WHERE code = %s", (new_name, college_code, code))
            mysql.connection.commit()
            return "Course updated successfully"
        except Exception as e:
            return f"Failed to update course: {str(e)}"

    @classmethod
    def delete_course(cls, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM course WHERE code = %s", (code,))
            mysql.connection.commit()
            return "Course and its students deleted successfully"
        except Exception as e:
            return f"Failed to delete course: {str(e)}"

    @classmethod
    def search_courses(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        query = """
        SELECT course.code AS course_code, course.name AS course_name, college.code AS college_code, college.name AS college_name
        FROM course
        INNER JOIN college ON course.college_code = college.code
        WHERE course.name LIKE %s OR course.code LIKE %s
        OR college.name LIKE %s OR college.code LIKE %s
        """
        search_query = f"%{search_query}%"
        cur.execute(query, (search_query, search_query, search_query, search_query))
        return cur.fetchall()



