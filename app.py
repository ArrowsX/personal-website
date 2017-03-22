from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def ic():
    return render_template('ic.html')

@app.route('/')
def tgbots():
    return render_template('tgbots.html')

@app.route('/')
def workshop():
    return render_template('workshop.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
