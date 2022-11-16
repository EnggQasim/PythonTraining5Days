from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>\
        <p>Pakistan</p>\
            Zinda bad"

@app.route("/about")
def about():
    return '''
    <h1>About Us</h1>
    Pakistan zinda bad!
    '''


if __name__=='__main__':
    app.run(debug=True)