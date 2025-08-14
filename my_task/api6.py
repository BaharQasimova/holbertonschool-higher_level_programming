from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/hello" method="post">
            Adini daxil et: <input type="text" name="username"><br>
            Soyadini daxil et: <input type="text" name="surname"><br>
            Yaşini daxil et: <input type="text" name="age"><br><br>
            <input type="submit" value="Hamisini göndər">
        </form>
    '''

@app.route('/hello', methods=['POST'])
def hello():
    username = request.form['username']
    surname = request.form['surname']
    age = request.form['age']
    return render_template('hello.html', name=username, surname=surname, age=age)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5300)
