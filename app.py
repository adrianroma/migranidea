from flask import Flask, render_template
from flask_cors import cross_origin

app = Flask(__name__, template_folder="templates")


# Source - https://stackoverflow.com/a/76508341
# Posted by imran3
# Retrieved 2026-02-18, License - CC BY-SA 4.0



@app.route("/")
@cross_origin(origins=["https://unpkg.com", "https://esm.sh"])
def index():
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)
