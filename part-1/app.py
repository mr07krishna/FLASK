from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Home page
@app.route("/")
@app.route("/home/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# Welcome page with dynamic name
@app.route("/welcome/<name>/")
def welcome(name):
    return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"

# Addition with a single number, corrected to cast num to int
@app.route("/addition/<int:num>/")
def addition(num):
    return f"<h1>Input is {num}, Output is {num + 10}</h1>"

# Addition with two numbers
@app.route("/addition_two/<int:num1>/<int:num2>/") #  also u add a float number here 
def addition_two(num1, num2):
    return f"<h1>{num1} + {num2} is {num1 + num2}</h1>"

# About page
@app.route("/about/")
def about(): 
    return "<h1>Welcome to the About Page!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
