from flask import Flask, render_template

app = Flask(__name__)
app.secret_key ="123"

@app.route('/')
def homepage():
    return render_template('homepg.html')


if __name__ == '__main__':
    app.run(port=4996)
