from flask import Flask, render_template, request
from utils import predict_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        prediction = predict_text(text)
        return render_template('main.html', text=text, prediction=prediction)
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def download():
    username = request.args.get('username')
    password = request.args.get('password')

    list_username = ['a', 'b', 'c']
    list_password = ['x', 'y', 'z']

    if username in list_username:
        id_user = list_username.index(username)

        if password == list_password[id_user]:

            return "Berhasil"
        else:

            return "password salah"
    else:

        return "username salah"

@app.route('/register', methods=['POST'])
def register():
    new_username = request.args.get('new_username')
    new_password = request.args.get('new_password')

    list_username = ['d', 'e', 'f']
    list_password = ['1', '2', '3']

    if new_username in list_username:
        return "Username sudah terdaftar"

    else:
        list_username.append(new_username)
        list_password.append(new_password)

        return f"Registrasi Berhasil. Halo, {new_username}!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
