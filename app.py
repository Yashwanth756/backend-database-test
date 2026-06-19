from flask import Flask, render_template, request, redirect
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")

    users = User.query.all()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)