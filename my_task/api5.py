from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Yasil Dunya!</h1>
    <p><a href="/Giris hisse">giris hisse</a></p>
    <p><a href="/Esas hisse">esas hisse</a></p>
    <p><a href="/Netice">netice</a></p>
    """

@app.route('/Giris hisse')
def giris_hisse():
    return """
    <h1>Giris hisse</h1>
    <p>Yasil Dunyaya xos gelmisiz!</p>
    <p><a href="/"> ilk sehifeye qayit</a></p>
    """

@app.route('/Esas hisse')
def esas_hisse():
    return """
    <h1>Esas hisse</h1>
    <p>Bu hissede yasil dunya ucun neler edilecek haqqinda fikirler olacaq.</p>
    <p><a href="/">ilk sehifeye qayit</a></p>
    """

@app.route('/Netice')
def netice():
    return """
    <h1>Netice</h1>
    <p>Yasil dunya layihesinin neticesi eks olunacaq.</p>
    <p><a href="/">ilk sehifeye qayit</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5100)