
from flask import Flask, render_template, request, jsonify
from flask import Flask
from db import c, conn
import requests
import json
import openai
import sqlite3
app = Flask(__name__, template_folder='templates',
            static_folder='static')
openai.api_key = ''


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/provider/dashboard')
def provider_dashboard():
    return "provider_dashboard"

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
        return render_template('submit_succesfully.html')
    return render_template("provider_submit.html")

@app.route('/volunteer/apply')
def volunteer_apply():
    c.execute("SELECT event.*, school.location, school.name, school.city, complete FROM event INNER JOIN school ON event.schid = school.schid")
    events = c.fetchall()
    for x in events:
        if x[-1]  == "TRUE":
            print(x[-1])
            events.remove(x)
    unique_locations = set(row[7] for row in events)

    return render_template("volunteer_dashboard.html", events=events, unique_locations=unique_locations)


@app.route('/volunteer/ranking') 
def volunteer_ranking():
    c.execute("SELECT volunteerid, firstname, lastname, points, location, RANK () OVER ( ORDER BY points DESC) Rank FROM volunteers ORDER BY Rank ASC")
    rows = c.fetchall()
   

    return render_template("volunteer_ranking.html", rows=rows, enumerate=enumerate)

@app.route('/volunteer/apply/<variable>')
def volunteer_apply_id(variable):
    c.execute('UPDATE event SET complete = "TRUE" WHERE event.eventid = ?', variable)
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
