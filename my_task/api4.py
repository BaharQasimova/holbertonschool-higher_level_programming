from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Salam!</h1>
    <p><a href="/haqqinda">Haqqinda</a></p>
    <p><a href="/elaqe">Elaqe</a></p>
    <p><a href="/layihe">Layihe</a></p>
    """

@app.route('/haqqinda')
def haqqinda():
    return """
    <h1>Haqqinda</h1>
    <p>Menim haqqimda melumatlar...</p>
    <p><a href="/">Ana sehifeye qayit</a></p>
    """

@app.route('/elaqe')
def elaqe():
    return """
    <h1>Elaqe</h1>
    <p>Elaqe melumatlari...</p>
    <p><a href="/">Ana sehifeye qayit</a></p>
    """

@app.route('/layihe')
def layihe():
    return """
    <h1>Layihe</h1>
    <p>Layihe melumatlari...</p>
    <p><a href="/">Ana sehifeye qayit</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=1400)