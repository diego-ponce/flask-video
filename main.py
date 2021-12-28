import os
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from app import app


@app.route("/")
def date_select_form():
    return render_template("video.html")


@app.route("/", methods=["POST"])
def select_videos_by_date():
    date_string = request.form.get("date")
    try:
        date.fromisoformat(date_string)
    except ValueError:
        flash("Invalid date - try again")
        return redirect(request.url)
    date_files = []
    for root, dirs, files in os.walk(app.config["MEDIA_FOLDER"]):
        for f in files:
            if date_string in f:
                filepath = os.path.join(root, f)
                filepath = os.path.relpath(filepath, start=app.config["MEDIA_FOLDER"])
                date_files.append(filepath)
    return render_template("video.html", date_files=date_files)


@app.route("/display/<path:filename>")
def display_video(filename):
    print(url_for("static", filename="media/" + filename))
    return redirect(url_for("static", filename="media/" + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)
