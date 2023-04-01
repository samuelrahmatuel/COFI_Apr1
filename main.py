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

@app.route('/download', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True, port=8080)
