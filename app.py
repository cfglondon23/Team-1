from flask import Flask

app = Flask(__name__)

@app.route('/')
# Dash Board
def hello():
    return 'Hello, World!'

@app.route('/provider/dashboard')
def provider_dashboard():
    return "provider_dashboard"

@app.route('/provider/submit')
def provider_submit():
    return "provider_submit"

@app.route('/volunteer/apply')
def volunteer_apply():
    return "volunteer_apply"

@app.route('volunteer/ranking')
def volunteer_ranking():
    return "volunteer_ranking"

if __name__ == '__main__':
    app.run()
