from flask import Flask, render_template, request
from flask import Flask
from db import c
import sqlite3
app = Flask(__name__, template_folder='templates',
            static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/provider/dashboard')
def provider_dashboard():
    return "provider_dashboard"

@app.route('/provider/submit', methods=['POST'])
def provider_submit():
    if request.method == "POST":
        title = request.form.get("title")
        school = request.form.get("school")
        description = request.form.get("description")
        location = request.form.get("location")
        city = request.form.get("city")

        # find the school id based on the school name, city and location
        queryString = 'SELECT * FROM school WHERE name = ? AND city = ? AND location = ?'
        c.execute(queryString, (school,city, location))
        school = c.fetchone()
        schoolId = school[0]

        c.execture(f"INSERT INTO event (name, schid, info) VALUES ('{title}', '{schoolId}', {description})")
        return render_template('submit_succesfully.html')
    return render_template("provider_submit.html")

@app.route('/volunteer/apply')
def volunteer_apply():
    return "volunteer_apply"

@app.route('/volunteer/ranking') 
def volunteer_ranking():
    return "volunteer_ranking"

if __name__ == '__main__':
    app.run()
