from flask import Flask, render_template, request, jsonify
from flask import Flask
from db import c
import requests
import json
import openai
app = Flask(__name__, template_folder='templates',
            static_folder='static')
openai.api_key = ''

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
    c.execute("SELECT volunteerid, firstname, lastname, points, location, RANK () OVER ( ORDER BY points DESC) Rank FROM volunteers ORDER BY Rank ASC")
    rows = c.fetchall()
    return render_template("volunteer_ranking.html", rows=rows, enumerate=enumerate)



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




