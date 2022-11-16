from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/signup", methods=['post','get'])
def user_detail():
    return render_template('signup.html')

@app.route('/signup_dealing', methods=['get','post'])
def signup_deal():
    if request.method == "GET":
        user_name = request.args.get('uname')
        email = request.args.get('email')
        details = request.args.get('details')
    if request.method == 'POST':
        user_name = request.form['uname']
        email = request.form['email']
        details = request.form['details']

        return f"Welcome Dear {user_name} <br> your Email {email}<br> Details:<br>{details}"


if __name__=='__main__':
    app.run(debug=True)