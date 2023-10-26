from flask import Flask, render_template, request, redirect, url_for, send_file
from pdf2docx import Converter


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/file", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf_file" in request.files:
            pdf_file = request.files["pdf_file"]
            if pdf_file.filename.endswith(".pdf"):
                pdf_path = pdf_file.filename
                pdf_file.save(pdf_path)
                word_path = "uploads/" + pdf_path.replace(".pdf", ".docx")
                word_name = pdf_file.filename.replace(".pdf", ".docx")

                cv = Converter(pdf_path)
                cv.convert(word_path, start=0, end=None)
                cv.close()

                return redirect(url_for("download", filename=word_name))
    return render_template("index.html")


@app.route("/download/<filename>")
def download(filename):
    return send_file("uploads/" + filename, as_attachment=True)


# main driver function
if __name__ == "__main__":
    app.run()
