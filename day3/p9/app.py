from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

data = [{'id':1,'name':'Qasim'},{'id':2,'name':'Asif'}]
author = "PAKISTAN"

@app.route("/detail")
def details():
    return render_template('detail.html', udata=data, auth=author)

if __name__=='__main__':
    app.run(debug=True)