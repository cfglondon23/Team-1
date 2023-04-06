from flask import Flask, render_template
from flask import Flask

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
    return "volunteer_apply"

@app.route('/volunteer/ranking')
def volunteer_ranking():
    return "volunteer_ranking"

if __name__ == '__main__':
    app.run()
