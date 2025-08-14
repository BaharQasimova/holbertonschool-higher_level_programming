from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Xos gelmisiz! Bura FLASK-dir."

@app.route('/salam', methods=['GET'])
def salam():
    ad = request.args.get('ad', 'Qonaq')
    return f"Salam, {ad}!"

@app.route('/gonder', methods=['POST'])
def gonder():
    ad = request.form.get('ad')
    if ad:
        return f"POST ile geldi: Salam, {ad}!"
    else:
        return "Zehmet olmasa, ad daxil edin."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=3005)