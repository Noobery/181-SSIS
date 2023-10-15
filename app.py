from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home_page():

    return render_template("students.html")

@app.route("/students")
def students():

    return render_template("students.html")

@app.route("/courses")
def CCS():

    return render_template("courses.html")

    

if __name__ == '__main__':
    app.run (host = '0,0,0,0', debug = True)