from flask import Flask, render_template, send_from_directory, request, session

from src.db.DB import DB

DB.setConfig("config.ini")
mydb = DB.connect()
app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code her
    return render_template('head.html', title='Accueil') + render_template('home.html')


# on veut autoriser les methodes POST et GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'mdp' in request.form:
            username = request.form['username']
            password = request.form['mdp']
            cursor = mydb.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s AND mdp = %s', (username, password))
            account = cursor.fetchone()
            if account:
                session['loggedin'] = True
                session['username'] = account[0]
                session['score'] = account[2]
                return render_template('head.html', title='Login') + render_template('loged.html',
                                                                                     user=session['username'])
            else:
                msg = 'Mauvais identifiant ou mot de passe !'
        else:
            msg = 'Veuillez remplir tous les champs !'
    return render_template('head.html', title='Login') + render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'mdp' in request.form:
            username = request.form['username']
            password = request.form['mdp']
            cursor = mydb.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', username)
            account = cursor.fetchone()
            if account:
                msg = 'Compte déjà existant !'
            else:
                cursor.execute('INSERT INTO users VALUES (%s, %s, 0)', (username, password))
                mydb.commit()
                msg = 'Vous êtes maintenant inscrit !'
        else:
            msg = 'Veuillez remplir tous les champs !'
    return render_template('head.html', title='Register') + render_template('register.html', msg=msg)


@app.route('/quizz', methods=['GET', 'POST'])
def quizz():
    html = render_template('head.html', title='Quizz')
    if session['loggedin']:
        html += """
        <audio src="audio/Dark_Mystery.mp3" type="audio/mpeg" loop=-1 autoplay></audio>
        <div id="quizz">
            <p>Salut {} ! Ce quizz comporte 4 questions. Chaque bonne réponse te donnera 3 points, une mauvaise t'en fera perdre 1.</p>
            <form id="formulaire" method="POST" action="/score">
        """.format(session['username'])

        mesQ = open("questions.csv", "r", encoding="utf-8")  # On ouvre le fichier contenant les questions
        mesQ.readline()
        Q = []
        for lig in mesQ:  # On parcourt ligne par ligne le fichier
            lig = lig.rstrip("\n")  # On retire le retour a la ligne
            vals = lig.split(";")  # On retire les ";"
            Q.append(vals)
        mesQ.close()  # On ferme le fichier
        # on ne garde que 4 questions aleatoires
        import random
        Q = random.sample(Q, 4)
        i = 1
        # on affiche le dictonnaire Q
        for q in Q:
            html += """
            <div class="question">
                <input type="hidden" name="Q{0}" value="{10}">
                <h3>Question {0}</h3>
                <p>{1}</p>
                <div class="reponses">
                    <input type="radio" name="Rep{0}" value="1" id="{2}">
                    <label for="{2}">{3}</label><br>
                    <input type="radio" name="Rep{0}" value="2" id="{4}">
                    <label for="{4}">{5}</label><br>
                    <input type="radio" name="Rep{0}" value="3" id="{6}">
                    <label for="{6}">{7}</label><br>
                    <input type="radio" name="Rep{0}" value="4" id="{8}">
                    <label for="{8}">{9}</label><br>
                </div>
            </div><br>
            """.format(i, q[1], "Q" + str(i) + "rep1", q[2], "Q" + str(i) + "rep2", q[3], "Q" + str(i) + "rep3", q[4],
                       "Q" + str(i) + "rep4", q[5], q[0])
            i += 1
        html += """
            <button type="submit" id="submit">Valider</button>
            </form>
        </div>
        """
    else:
        html += render_template('home.html')
    return html


@app.route('/score', methods=['POST'])
def score():
    if session['loggedin']:
        if request.method == 'POST' :
            if 'Rep1' in request.form and 'Rep2' in request.form and 'Rep3' in request.form and 'Rep4' in request.form :
                score = 0
                mesQ = open("questions.csv", "r", encoding="utf-8")  # On ouvre le fichier contenant les questions
                mesQ.readline()
                Q = {}
                for lig in mesQ:  # On parcourt ligne par ligne le fichier
                    lig = lig.rstrip("\n")  # On retire le retour a la ligne
                    vals = lig.split(";")  # On retire les ";"
                    Q[vals[0]] = vals
                mesQ.close()  # On ferme le fichier
                for i in range(1, 5):
                    q = Q[request.form['Q' + str(i)]]
                    print(request.form['Rep' + str(i)])
                    if request.form['Rep' + str(i)] == q[6]:
                        score += 3
                    else:
                        score -= 1
                if score < 0:
                    score = 0
                session['score'] += score
                cursor = mydb.cursor()
                cursor.execute('UPDATE users SET score = %s WHERE username = %s', (session['score'], session['username']))
                mydb.commit()
                cursor.execute('SELECT * FROM users ORDER BY score DESC')
                classement = cursor.fetchall()
                html = """
                <div id="quizz">
                    <p>Vous avez fait un scrore de {}/12 ! Votre score total est de {}</p>
                    <div class="classement">
                        <p>Classement :</p>
                        <ol>""".format(score, session['score'])
                for i in range(len(classement)):
                    html += """<li>{}</li>""".format(classement[i][0])
                html += """</ol>
                    </div><p>Correction :</p>"""
                for i in range(1, 5):
                    html += """
                    <p>Question {} : {}</p>
                    <p>Réponse juste : {}</p><br>""".format(i, Q[request.form['Q' + str(i)]][1],
                                                            Q[request.form['Q' + str(i)]][
                                                                int(Q[request.form['Q' + str(i)]][6]) + 1])
                html += """
                    <form method="POST" action="/quizz">
                        <button>Nouvelle partie</button>
                    </form>
                    <br>
                    <form method="POST" action="/add-question">
                        <button>Proposer une nouvelle question</button>
                    </form>
                </div>"""
                return render_template('head.html', title='Score') + html
            else:
                return render_template('head.html', title='Score') + "Vous n'avez pas répondu à toutes les questions !"
    return render_template('head.html', title='Score') + render_template('home.html')


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    return render_template('head.html', title='Add Question') + render_template('add-question.html')


# on veut pouvoir acceder au dossier css, img, src et audio
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/src/js/<path:path>')
def send_src(path):
    return send_from_directory('src/js', path)


@app.route('/audio/<path:path>')
def send_audio(path):
    return send_from_directory('audio', path)


if __name__ == '__main__':
    app.run()
