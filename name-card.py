from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def display_nc():
    return render_template("nc_index.html")


app.run(debug=True)
