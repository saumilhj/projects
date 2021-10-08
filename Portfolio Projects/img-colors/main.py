from colorthief import ColorThief
import os
from flask import *

app = Flask(__name__)
UPLOAD_FOLDER = "static/images"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        file = request.files['image']
        ext = file.filename.split(".")[1].lower()
        if ext in ALLOWED_EXTENSIONS:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            palette = []
            color_thief = ColorThief(f"./static/images/{file.filename}")
            temp_palette = color_thief.get_palette(color_count=10)
            for color in temp_palette:
                palette.append('#%02x%02x%02x' % color)
            return render_template("index.html", showimage=f"/static/images/{file.filename}", colors=palette)

        else:
            return {'error': 'File uploaded not an image'}


if __name__ == "__main__":
    app.run(debug=True)
