from flask import Flask
from flask import send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def get_image():
    list_files = subprocess.run(["fswebcam", "-r", "1280x720", "image.jpg"])
    filename = 'image.jpg'
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
