from flask import Flask, render_template
from flask_cors import CORS,cross_origin

app = Flask(__name__, template_folder="templates")


# Source - https://stackoverflow.com/a/76508341
# Posted by imran3
# Retrieved 2026-02-18, License - CC BY-SA 4.0

CORS(app)

@app.route("/")
@cross_origin()
def index():
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)
