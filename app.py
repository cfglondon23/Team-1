from flask import Flask, render_template
from flask import Flask
<<<<<<< HEAD

=======
from db import c
>>>>>>> database
app = Flask(__name__, template_folder='templates',
            static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/provider/dashboard')
def provider_dashboard():
    return "provider_dashboard"

@app.route('/provider/submit')
def provider_submit():
    return "provider_submit"

@app.route('/volunteer/apply')
def volunteer_apply():
    c.execute("SELECT event.*, school.location, school.name, school.city FROM event INNER JOIN school ON event.schid = school.schid")
    events = c.fetchall()
    return render_template("volunteer_dashboard.html", events=events)


@app.route('/volunteer/ranking')
def volunteer_ranking():
<<<<<<< HEAD
    return "volunteer_ranking"
=======
    c.execute("SELECT volunteerid, firstname, lastname, points, location, RANK () OVER ( ORDER BY points DESC) Rank FROM volunteers ORDER BY Rank ASC")
    rows = c.fetchall()
    return render_template("volunteer_ranking.html", rows=rows, enumerate=enumerate)
>>>>>>> database

if __name__ == '__main__':
    app.run(debug=True)