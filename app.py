from website import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

"""from flask import Flask, render_template, url_for, request, Blueprint
from flask_mysql_connector import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Baptist69!'
app.config['MYSQL_DATABASE'] = 'SSIS'

mysql = MySQL(app)

@app.route("/")
def home_page():
    return render_template("students.html")

@app.route("/students")
def students():    
    return render_template("students.html")

@app.route("/colleges", methods=["GET", "POST"])
def colleges():
    cur = mysql.new_cursor(dictionary=True)
    
    if request.method == "POST": 
        name = request.form.get("collegeName")
        code = request.form.get("collegeCode")
        cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
        mysql.connection.commit()
        
    cur.execute("SELECT * FROM college")
    colleges = cur.fetchall()
    
    return render_template("colleges.html", colleges=colleges)

@app.route("/courses")
def courses():

    return render_template("courses.html")
    
    

if __name__ == '__app__':
    app.run (host = '0,0,0,0', debug = True)

    """