from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from db import c, conn
import openai


app = Flask(__name__, template_folder='templates',
            static_folder='static')
openai.api_key = ''


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/provider/dashboard', methods=['GET','POST'])
def provider_dashboard():
    if request.method=='POST':
        return redirect(url_for('provider_submit'))
    
    else:
        # Fetch the last 2 'Done' events from the database, selecting only desired columns
        c.execute("SELECT eventid, schid, name, info FROM event WHERE complete='TRUE' ORDER BY eventid")
        done_events = c.fetchall()

        # Fetch the first 3 'In Progress' events from the database, selecting only desired columns
        c.execute("SELECT eventid, schid, name, info, required, sofar FROM event WHERE complete='FALSE'")
        in_progress_events = c.fetchall()

        # Render the template and pass the fetched event data to be used in the template
        return render_template('provider_dashboard.html', done_events=done_events, in_progress_events=in_progress_events)

@app.route('/provider/submit', methods=['POST','GET'])
def provider_submit():
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")
        location = request.form.get("location")
        city = request.form.get("city")

        # find the school id based on the school name, city and location
        queryString = 'SELECT * FROM school WHERE schid = ?'
        schid = 1
        c.execute(queryString, (schid,))

        school = c.fetchone()
        schoolId = school[0]
    
        c.execute(f"INSERT INTO event (name, schid, info) VALUES ('{title}', '{schoolId}', '{description}')")
        conn.commit()
        return redirect(url_for('provider_dashboard'))
    return render_template("provider_submit.html")

@app.route('/volunteer/apply')
def volunteer_apply():
    c.execute("SELECT event.*, school.location, school.name, school.city, complete FROM event INNER JOIN school ON event.schid = school.schid WHERE complete != 'TRUE'")
    events = c.fetchall()
    
    unique_locations = set(row[7] for row in events)

    return render_template("volunteer_dashboard.html", events=events, unique_locations=unique_locations)


@app.route('/volunteer/ranking') 
def volunteer_ranking():
    c.execute("SELECT volunteerid, firstname, lastname, points, location, RANK () OVER ( ORDER BY points DESC) Rank FROM volunteers ORDER BY Rank ASC")
    rows = c.fetchall()
   

    return render_template("volunteer_ranking.html", rows=rows, enumerate=enumerate)

@app.route('/volunteer/apply/<variable>')
def volunteer_apply_id(variable):
    c.execute('UPDATE event SET complete = "TRUE" WHERE eventid = ?', (variable,))
    return render_template("volunteer_apply.html")


@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form["user_input"]

    # Create a chat message with the user input as the content
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}]

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with the correct chat model name
        messages=messages,
        max_tokens=750,
        n=1,
        stop=None,
        temperature=1.0,
        top_p=1,
    )

    # Extract the assistant's response
    generated_text = response.choices[0].message['content'].strip()
    print(generated_text)
    return {"generated_text": generated_text}


@app.route('/learn/')
def learn():

    return render_template("learn.html")

if __name__ == '__main__':
    app.run(debug=True)
