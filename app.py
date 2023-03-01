from flask import Flask, render_template, send_from_directory, request, session

from src.db.DB import DB

DB.setConfig("config.ini")
mydb = DB.connect()
app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route('/')
def hello_world():  # put application's code her
    return render_template('head.html', title='Accueil') + render_template('home.html')


# on veut autoriser les methodes POST et GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'mdp' in request.form:
        username = request.form['username']
        password = request.form['mdp']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND mdp = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account[0]
            session['score'] = account[2]
            return render_template('head.html', title='Login') + render_template('loged.html', user=session['username'])
        else:
            msg = 'Mauvais identifiant ou mot de passe !'
    return render_template('head.html', title='Login') + render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('head.html', title='Register') + render_template('register.html')


@app.route('/quizz')
def quizz():
    return 'Quizz'


@app.route('/score', methods=['POST'])
def score():
    return 'Score'


@app.route('/add-question')
def add_question():
    return 'Add question'


# on veut pouvoir acceder au dossier css, img, src
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/src/js/<path:path>')
def send_src(path):
    return send_from_directory('src/js', path)


if __name__ == '__main__':
    app.run()
