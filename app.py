from flask import Flask, render_template
from flask import Flask
from db import c
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

@app.route('/volunteer/apply/<city>')
def volunteer_apply(city):
    city = str(city)
    # Get the school id for that city
    c.execute("SELECT * FROM school WHERE city = ?", (city,))
    school_id_in_the_city = [x[0] for x in c.fetchall()]
    # Check if the city has any schools
    if not school_id_in_the_city:
        return "No schools found in the selected city"
    statement = f"SELECT * FROM event WHERE schid IN ({','.join('?'*len(school_id_in_the_city))})"
    c.execute(statement, school_id_in_the_city)
    events = c.fetchall()
    return render_template("volunteer_dashboard.html", events=events)



@app.route('/volunteer/ranking')
def volunteer_ranking():
    c.execute("SELECT volunteerid, firstname, lastname, points, location, RANK () OVER ( ORDER BY points DESC) Rank FROM volunteers ORDER BY Rank ASC")
    rows = c.fetchall()
    return render_template("volunteer_ranking.html", rows=rows, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)