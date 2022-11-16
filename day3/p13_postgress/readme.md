#SQLAlchemy 
* Installation
    * `pip install -U Flask-SQLAlchemy`
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
```
**stored in the app’s instance folder.**<br>
The **db** object gives you access to the **db.Model** class to define models, and the **db.session** to execute queries.
## Define Models¶
* Subclass `db.Model` to define a model class. The db object makes the names in sqlalchemy and `sqlalchemy.orm `available for convenience, such as `db.Column`. The model will generate a table name by converting the CamelCase class name to snake_case.


```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
```
* Next app.app_context() will create databae and all table in database
```
with app.app_context():
    db.create_all()
```
## Query the Data¶
```
@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user/delete.html", user=user)
```

* **user/menu.html**
```
<ul>
    <li><a href="{{url_for('user_list')}}">Users</a></li>
    <li><a href="{{url_for('user_create')}}">Add new user</a></li>

</ul>
```
* **users/create.html**
```
{%include 'user/menu.html'%}
<form method="post">
    <input type="text" name="username" placeholder="User name"><br>
    <input type="email" name="email" placeholder="abc@gmail.com"><br>
    <input type="submit" value="Create">
</form>
```
* **user/detail.html**
```
{%include 'user/menu.html'%}
<h1>User Details</h1>
Hell Dear, {{user.username}}!<br>
Your email addres is: {{user.email}}

```

* **user/list.html**
```
{%include 'user/menu.html'%}
{%for row in users%}
<ul>
    <li>{{row.username}}
        <ul>
            <li>{{row.email}}</li>
            <li><a href="/user/{{row.id}}/delete">Delete</a></li>
        </ul>
    </li>
    
</ul>

{%endfor%}
```
* **user/delete.html**
```
{%include 'user/menu.html'%}
<form method="post">
    <input type="text" name="username" value="{{user.username}}"><br>
    <input type="email" name="email" value="{{user.email}}"><br>
    <input type="submit" value="Are you sure? you want to Delete?">
</form>
```



