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
    def get_students(cls, page_size: int, page_number: int):
        print(page_size, page_number)
        offset = (page_number - 1) * page_size
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
                LIMIT %s OFFSET %s
            """, [page_size, offset])

            results = cur.fetchall()
             
            count_cur = mysql.new_cursor(dictionary=True)
            count_cur.execute("""
                SELECT COUNT(*) as student_count FROM student
            """)
            total_count = count_cur.fetchone()['student_count']
            
            has_prev = offset > 0
            has_next = (offset + page_size) < total_count

            return {
                'results': results,
                'total_count': total_count,
                'has_prev': has_prev,
                'has_next': has_next
            }
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
