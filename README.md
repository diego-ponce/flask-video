# flask video - a video player website

Inspired by https://roytuts.com/upload-and-play-video-using-flask/

## Quickstart

```
# clone this repo
git clone <github url>

# cd into the repo
cd flask-video

# set up a virtual env
python3.9 -m venv venv && source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the webserver
python app.py

```
Select a date and submit - if there is a video for that date it will be displayed. If there are multiple videos for that date, a new `<div>` will be created for each video dynamically.

## Notes

- This project is under development - the Flask app is defaulted to debug (not meant for production)

- Videos are selected by having the ISO date in the filename (e.g., `2021-12-17`)

- Videos are available between 2021-12-17 and 2021-12-25 in this example repo

