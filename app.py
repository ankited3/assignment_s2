from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    file_info = None
    animal = None

    if request.method == "POST":
        # Handle animal selection
        animal = request.form.get("animal")

        # Handle file upload
        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename != "":
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                file_info = {
                    "name": file.filename,
                    "size": os.path.getsize(filepath),
                    "type": file.content_type
                }

    return render_template("index.html", animal=animal, file_info=file_info)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
