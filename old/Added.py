#! C:\python\python311\python.exe
# -*- coding: utf8 -*-
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html")
print()

donnees = cgi.FieldStorage()  # On récupère le texte saisi dans le formulaire
quest = donnees.getvalue("question")
rep1 = donnees.getvalue("Rep1")
rep2 = donnees.getvalue("Rep2")
rep3 = donnees.getvalue("Rep3")
rep4 = donnees.getvalue("Rep4")
cor = donnees.getvalue("correction")
log = donnees.getvalue("login")

monF = open("questions.csv", "r", encoding="utf-8")  # On ouvre le fichier contenant les questions
Q = monF.readlines()
k = len(
    Q)  # On prend la longueur du fichier pour en faire la numéro de la nouvelle question puisque le première ligne est vide
monF.close()  # On ferme le fichier

# On confirme que la question du joueur à été ajouté

if log != None:  # On fait les test pour savoir si le joueur est connecté
    monF = open("questions.csv", "a", encoding="utf-8")  # On met à jour le fichier
    monF.write("\n" + str(k) + ";" + quest + ";" + rep1 + ";" + rep2 + ";" + rep3 + ";" + rep4 + ";" + cor)
    monF.close()
    print('''<!DOCTYPE html>

                <html>
                	<head>
                		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
                		<title>Quizz</title>
                		<link rel="stylesheet" type="text/css" href="css/main.css"/>
                        <link rel="icon" type="image/png" href="img/icon.png"/>
                		<script type="text/javascript" src="fonctions.js"></script>
                	</head>

                	<body>
                        <div id="content">
      		                <p>Félicitation {} ! Votre question est maintenant ajoutée à notre Quizz ! Vous pouvez en proposer une autre ou commencer une nouvelle partie !</p>
                            <form method="POST" action="AddQuestions.py">
                                <input type="hidden" name="login" value="{}"/>
                                <button>Ajouter une autre question</button>
                            </form>
                            <form method="POST" action="jeu.py">
                                <input type="hidden" name="login" value="{}"/>
                                <button>Nouvelle partie</button>
                            </form>
                        </div>
                	</body>
                </html>
    '''.format(log, log, log))
else:  # Sinon on affiche une autre page lui demandant de se connecter ou de s'inscrire
    print('''
            <!DOCTYPE html>
                <html>
                	<head>
                		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
                		<title>Quizz</title>
                		<link rel="stylesheet" type="text/css" href="css/main.css"/>
                        <link rel="icon" type="image/png" href="img/icon.png"/>
                		<script type="text/javascript" src="fonctions.js"></script>
                	</head>

                	<body>
                        <div id="content">
                			<p>Salut !</p>
                			<p><em>Pour pouvoir <mark>ajouter des questions</mark> il faut être <strong>inscrit</strong> !</em></p>
                			<form method="POST" action="register.html">
                				<button>S'inscrire</button>
                			</form>
                			<form method="POST" action="login.html">
                				<button>Se connecter</button>
                			</form>
                		</div>
                	</body>
                </html>
    ''')
