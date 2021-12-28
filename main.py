import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from app import app


@app.route("/")
def upload_form():
    return render_template("upload.html")


# TODO post date, return files on that date
@app.route("/", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        flash("Video successfully uploaded and displayed below")
        return render_template("upload.html", filename=filename)


@app.route("/display/<filename>")
def display_video(filename):
    return redirect(url_for("static", filename="uploads/" + filename), code=301)


if __name__ == "__main__":
    app.run()
