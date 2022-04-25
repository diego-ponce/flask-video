import os
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from app import app


def sort_camera_location(filename):
    south_to_east = {
        "Portland_-_8th_at_Division": 0,
        "12th_at_Clinton": 1,
        "11th_at_Milwaukie_N": 2,
        "I-5_at_Morrison": 3,
        "I-84_at_Grand": 4,
        "I-84_at_Metro_Bldg.": 5,
        "I-84_at_37th": 6,
        "I-84_at_53rd": 7,
        "I-84_at_67th": 8,
        "I-84_at_Halsey": 9,
        "I-84_at_82nd": 10,
        "I-84_at_148th": 11,
        "I-84_at_223rd": 12,
    }
    try:
        res = [south_to_east[loc] for loc in south_to_east if loc in filename][0]
    except IndexError:
        res = 9999
    return res


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
    date_files.sort(key=sort_camera_location)
    return render_template("video.html", date_files=date_files)


@app.route("/display/<path:filename>")
def display_video(filename):
    print(url_for("static", filename="media/" + filename))
    return redirect(url_for("static", filename="media/" + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)
