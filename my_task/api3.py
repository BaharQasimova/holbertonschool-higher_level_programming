from flask import Flask

app = Flask(__name__)

@app.route('/')
def info():
    html_text = """
    <b>Menim haqqimda:</b><br>
    Ad: Bahar<br>
    Soyad: Qasimova<br>
    Yas: 20
    """
    return html_text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=4050)