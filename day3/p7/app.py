from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/user/<name>/<id>")
def user_detail(name:str, id:int):
    return f"Hell Dear, {name} Welcome! {id}"

if __name__=='__main__':
    app.run(debug=True)