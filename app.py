from flask import Flask, render_template, send_from_directory, request, session

from src.db.DB import DB

mydb = DB.connect()
app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route('/')
def home():  
    if session.get('loggedin'):
        return render_template('head.html', title='Accueil') + render_template('loged.html', user=session['username'])
    return render_template('head.html', title='Accueil') + render_template('home.html')


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
    if session.get('loggedin'):
        html += """
        <audio src="audio/Dark_Mystery.mp3" type="audio/mpeg" loop=-1 autoplay></audio>
        <div id="quizz">
            <p>Salut {} ! Ce quizz comporte 4 questions. Chaque bonne réponse te donnera 3 points, une mauvaise t'en fera perdre 1.</p>
            <form id="formulaire" method="POST" action="/score">
        """.format(session['username'])

        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM questions')
        Q = cursor.fetchall()
        import random
        Q = random.sample(Q, 4)
        i = 1
        # on affiche le dictonnaire Q
        for q in Q:
            # on met les questions dans le formulaire et en session
            session['Q' + str(i)] = q[1]
            session['Q' + str(i) + 'rep1'] = q[2]
            session['Q' + str(i) + 'rep2'] = q[3]
            session['Q' + str(i) + 'rep3'] = q[4]
            session['Q' + str(i) + 'rep4'] = q[5]
            session['Q' + str(i) + 'repJuste'] = q[6]
            html += """
            <div class="question">
                <input type="hidden" name="Q{0}" value="{10}">
                <h3>Question {0}</h3>
                <p>{1}</p>
                <div class="reponses">
                    <input type="radio" name="Rep{0}" value="1" id="{2}" checked>
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
    if session.get('loggedin'):
        if request.method == 'POST':
            if 'Rep1' in request.form and 'Rep2' in request.form and 'Rep3' in request.form and 'Rep4' in request.form:
                score = 0
                for i in range(1, 5):
                    if int(request.form['Rep' + str(i)]) == session['Q' + str(i) + 'repJuste']:
                        score += 3
                    else:
                        score -= 1
                if score < 0:
                    score = 0
                session['score'] += score
                cursor = mydb.cursor()
                cursor.execute('UPDATE users SET score = %s WHERE username = %s',
                               (session['score'], session['username']))
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
                    html += """<li>{} : {} pts</li>""".format(classement[i][0], classement[i][2])
                html += """</ol>
                    </div><p>Correction :</p>"""
                for i in range(1, 5):
                    html += """
                    <p>Question {} : {}</p>
                    <p>Réponse juste : {}</p><br>""".format(i, session['Q' + str(i)],
                                                            session['Q' + str(i) + 'rep' + str(
                                                                session['Q' + str(i) + 'repJuste'])])
                html += """
                    <a class="button" href="/quizz">Nouvelle partie</a>
                    <a class="button" href="/add-question">Proposer une nouvelle question</a>
                </div>"""
                return render_template('head.html', title='Score') + html
            else:
                return render_template('head.html', title='Score') + "Vous n'avez pas répondu à toutes les questions !"
    return render_template('head.html', title='Score') + render_template('home.html')


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if session.get('loggedin'):
        if request.method == 'POST':
            cursor = mydb.cursor()
            cursor.execute(
                'INSERT INTO questions (question, rep1, rep2, rep3, rep4, repJuste) VALUES (%s, %s, %s, %s, %s, %s)', (
                    request.form['question'], request.form['rep1'], request.form['rep2'], request.form['rep3'],
                    request.form['rep4'], int(request.form['correction'])))
            mydb.commit()
            return render_template('head.html', title='Add Question') + render_template('added.html',
                                                                                        user=session['username'])
    return render_template('head.html', title='Add Question') + render_template('add-question.html')


@app.route('/profil', methods=['GET', 'POST'])
def profil():
    if request.method == 'POST':
        # on supprime la session
        session.pop('loggedin', None)
        session.pop('username', None)
        session.pop('score', None)
        return render_template('head.html', title='Profil') + "Vous êtes déconnecté !" + render_template('home.html')
    else:
        if session.get('loggedin'):
            return render_template('head.html', title='Profil') + render_template('profil.html',
                                                                                  user=session['username'],
                                                                                  score=session['score'])
    return render_template('head.html', title='Profil') + "Vous n'êtes pas connecté !" + render_template('home.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if session.get('loggedin'):
        cursor = mydb.cursor()
        cursor.execute('DELETE FROM users WHERE username = %s', session['username'])
        mydb.commit()
        # on supprime la session
        session.pop('loggedin', None)
        session.pop('username', None)
        session.pop('score', None)
        return render_template('head.html', title='Delete') + "Votre compte a été supprimé !" + render_template(
            'home.html')
    return render_template('head.html', title='Delete') + "Vous n'êtes pas connecté !" + render_template('home.html')


# acceder au dossier css, img, src et audio
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

# on lance l'application
if __name__ == '__main__':
    app.run()
