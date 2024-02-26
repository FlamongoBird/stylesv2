from flask import Flask, send_file


app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "DELETE", "PUT"])
def serve_css():
    return send_file("output.css")

app.run("localhost", 8000)