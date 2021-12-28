from flask import Flask

MEDIA_FOLDER = "static/media"

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["MEDIA_FOLDER"] = MEDIA_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
