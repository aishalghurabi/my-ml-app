from flask import Flask, render_template, request
import os
from model import predict

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            output_path = predict(filepath)

            return render_template("index.html",
                                   input_image=filepath,
                                   output_image=output_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)