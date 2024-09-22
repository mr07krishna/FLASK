from flask import Flask, render_template
from employees import employees_data

# Create the Flask app
app = Flask(__name__)

# Home page
@app.route("/")
@app.route("/home/")
def home():
    return render_template(
         "home.html", 
         title="Home")

# Welcome page with dynamic name
@app.route("/welcome/<name>/")
def welcome(name):
    return render_template(
         "welcome.html", 
         title="Welcome", 
         name=name)

# About page
@app.route("/about/")
def about():
    return render_template(
         "about.html", 
         title="About")

# employees page
@app.route("/employees/")
def employees():
	return render_template(
		"employees.html",
		title="Employees",
		emps=employees_data
    )
    
# employees/Managers page
@app.route("/employees/managers")
def managers():
	return render_template(
		"managers.html",
		title="Managers",
		emps=employees_data
    )

    


# Evaluate page
@app.route("/evaluate/<int:num>/")
def evaluate(num):
    return render_template(
         "evaluate.html",
         title="Evaluate", 
         number=num
         )

if __name__ == "__main__":
    app.run(debug=True)
