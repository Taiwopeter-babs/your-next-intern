#!/usr/bin/python3
"""test schools loading with flask"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/intern-signup")
def load_schools():
    schools = storage.all("School").values()
    return render_template("intern_signup.html", schools=schools)


if __name__ == "__main__":
    app.run()
