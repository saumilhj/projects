import requests as req
from flask import *
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = YOUR_DOWNLOAD_LOCATION
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        url = request.form.get("input-url")
        res = req.get(f"https://qrtag.net/api/qr.png?url={url}")
        with open("qr_transparent.png", "wb") as f:
            f.write(res.content)
        return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], "qr_transparent.png"), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
