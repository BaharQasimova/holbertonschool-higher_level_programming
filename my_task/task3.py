

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return"<b>Salam, dunya!</b>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1400)

