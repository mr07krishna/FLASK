from flask import Flask, render_template
from forms import SignupForms, LoginForms

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForms()
    if form.validate_on_submit():
        # Handle form submission, e.g., save data to the database
        pass
    return render_template("signup.html", title="Sign Up", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        # Handle form submission, e.g., log in the user
        pass
    return render_template("login.html", title="Log In", form=form)

if __name__ == "__main__":
    app.run(debug=True)
