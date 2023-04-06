from flask import Flask, render_template, request, redirect, url_for
from db import c, conn

app = Flask(__name__, template_folder='templates',
            static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/provider/dashboard', methods=['GET','POST'])
def provider_dashboard():
    if request.method=='POST':
        return redirect(url_for('provider_submit'))
    
    else:
        # Fetch the last 2 'Done' events from the database, selecting only desired columns
        c.execute("SELECT eventid, schid, name, info FROM event WHERE complete='TRUE' ORDER BY eventid DESC LIMIT 2")
        done_events = c.fetchall()

        # Fetch the first 3 'In Progress' events from the database, selecting only desired columns
        c.execute("SELECT eventid, schid, name, info FROM event WHERE complete='FALSE' LIMIT 3")
        in_progress_events = c.fetchall()

        # Render the template and pass the fetched event data to be used in the template
        return render_template('provider_dashboard.html', done_events=done_events, in_progress_events=in_progress_events)

@app.route('/provider/submit')
def provider_submit():
    return "provider_submit"

@app.route('/volunteer/apply')
def volunteer_apply():
    return "volunteer_apply"

@app.route('/volunteer/ranking')
def volunteer_ranking():
    return "volunteer_ranking"

if __name__ == '__main__':
    app.run()
