from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form['name_input'])+ ", great to see you")
	return render_template("index.html")

@app.route("/worldcelebzone")
def OGUNLEYE():
	return redirect("https://www.worldcelebzone.com.ng")

@app.route("/mealsoz")
def test():
	return redirect("https://www.mealsoz.com")