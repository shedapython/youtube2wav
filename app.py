from flask import Flask, request, jsonify, render_template
from downloader import download_youtube
import os

app = Flask(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    urls = data.get("urls", [])
    if not urls:
        return jsonify({"error": "No URLs provided"}), 400

    download_youtube(urls, DOWNLOAD_DIR)
    return jsonify({"message": "Download complete", "saved_to": DOWNLOAD_DIR})

if __name__ == "__main__":
    app.run(debug=True)
