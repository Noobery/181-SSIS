from website import mysql

class CollegeModel:
    @classmethod
    def create_college(cls, name, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
            mysql.connection.commit()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create college: {str(e)}"

    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        return colleges

    @classmethod
    def delete_college(cls, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM college WHERE code = %s", (code,))
            mysql.connection.commit()
            return "College and its courses deleted successfully"
        except Exception as e:
            return f"Failed to delete college: {str(e)}"


    @classmethod
    def update_college(cls, code, new_name):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE college SET name = %s WHERE code = %s", (new_name, code))
            mysql.connection.commit()
            return "College updated successfully"
        except Exception as e:
            return f"Failed to update college: {str(e)}"
        
    @classmethod
    def search_colleges(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name FROM college WHERE name LIKE %s OR code LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        colleges = cur.fetchall()
        return colleges

    