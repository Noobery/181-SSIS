from website import mysql

class StudentModel:
    @classmethod
    def create_student(cls, id, firstname, lastname, course_code, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO student (id, firstname, lastname, course_code, year, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id, firstname, lastname, course_code, year, gender))
            mysql.connection.commit()
            return "Student created successfully"
        except Exception as e:
            return f"Failed to create student: {str(e)}"

    @classmethod
    def get_students(cls):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("""
                SELECT student.id, student.firstname, student.lastname,
                       student.course_code, student.year, student.gender,
                       course.name AS course_name, course.code AS course_code,
                       college.name AS college_name, college.code AS college_code
                FROM student
                INNER JOIN course ON student.course_code = course.code
                INNER JOIN college ON course.college_code = college.code
            """)
            students = cur.fetchall()
            return students
        except Exception as e:
            return f"Failed to retrieve students: {str(e)}"
        
    @classmethod
    def delete_student(cls, id):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM student WHERE id = %s", (id,))
            mysql.connection.commit()
            return "Student deleted successfully"
        except Exception as e:
            return f"Failed to delete student: {str(e)}"

    @classmethod
    def update_student(cls, id, firstname, lastname, course_code, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE student SET firstname = %s, lastname = %s, course_code = %s, year = %s, gender = %s WHERE id = %s", 
                        (firstname, lastname, course_code, year, gender, id))
            mysql.connection.commit()
            return "Student updated successfully"
        except Exception as e:
            return f"Failed to update student: {str(e)}"
