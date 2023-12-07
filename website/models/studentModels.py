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
                    student.profile_pic_url,
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

    @classmethod
    def search_students(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        query = """
        SELECT student.id, student.profile_pic_url, student.firstname, student.lastname, course.code AS course_code, course.name AS course_name, student.year, student.gender, college.code AS college_code, college.name AS college_name
        FROM student
        INNER JOIN course ON student.course_code = course.code
        INNER JOIN college ON course.college_code = college.code
        WHERE (student.id LIKE %s
        OR student.firstname LIKE %s
        OR student.lastname LIKE %s
        OR course.name LIKE %s
        OR course.code LIKE %s
        OR college.name LIKE %s
        OR college.code LIKE %s
        OR student.year LIKE %s
        OR student.gender LIKE %s)
        """
        search_query = f"%{search_query}%"
        cur.execute(query, (search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query))
        return cur.fetchall()

    @classmethod
    def update_student_profile_pic(cls, student_id, profile_pic_url):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE student SET profile_pic_url = %s WHERE id = %s",
                        (profile_pic_url, student_id))
            mysql.connection.commit()
            return "Profile picture updated successfully"
        except Exception as e:
            return f"Failed to update profile picture: {str(e)}"
        
    def get_student_profile_pic_url(cls, student_id):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("SELECT profile_pic_url FROM student WHERE id = %s", (student_id,))
            result = cur.fetchone()
            return result['profile_pic_url'] if result else None
        except Exception as e:
            return None