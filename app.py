from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():

	val1 = datetime.today().strftime("%Y-%m-%d %H:%M:%S %p")

	# return render_template("index.html", now=datetime.now())
	return render_template("index.html", now=val1)


if __name__ == "__main__":
	app.run()