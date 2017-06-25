from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ic')
def ic():
    return render_template('ic.html')

@app.route('/telegram')
def tgbots():
    return render_template('tgbots.html')

@app.route('/petwalk')
def petwalk():
    return render_template('petwalk.html')

if __name__ == '__main__':
    app.run(debug=True)
