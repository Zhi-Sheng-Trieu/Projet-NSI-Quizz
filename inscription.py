#! C:\python\python311\python.exe
# -*- coding: utf8 -*-
from src.db import DB
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html")
print()

donneesPlayer = db.ouvrir("liste.csv")  # On récupère les données du fichier csv

donnees = cgi.FieldStorage()  # On recupere le texte saisi dans le formulaire
log = donnees.getvalue("login")  # On le transforme en chaine de caracteres e
Mdp = donnees.getvalue("mdp")

borderC1 = ""  # On cree des variables vides contenant la couleur du cadre du formulaire
borderC2 = ""
msg1 = ""  # On cree une variable vide pour le message d'erreur pour le login
msg2 = ""  # On cree une variable vide pour le message d'erreur pour le mdp
msg3 = ""  # On cree une variable vide pour le message d'erreur si le login est déjà pris
submit = "return false"  # On met par défaut le return en return false

if log != None and log != " ":  # On fait un test pour savoir si l'identifiant est valide
    if len(Mdp) >= 8:  # On fait un autre test pour le mot de passe
        if log in donneesPlayer:  # On fait un test pour savoir si le login saisit est déjà pris
            msg3 = "Ce login est deja pris"  # Si oui on fait un message d'erreur
        else:
            submit = "return true"
    else:
        borderC2 = "red"  # On change la varible borderC2 qui vaudra "red" et on fait un message d'erreur si le Mdp est invalide
        msg2 = "Il faut saisir un mot de passe faisant au moins 8 caractères. "
else:
    borderC1 = "red"  # On change la varible borderC1 qui vaudra "red" et on fait un message d'erreur si le login est invalide
    msg1 = "Il faut saisir un identifiant valide. "

if submit != "return false":  # Si le joueur peut être inscrit on met à jour le fichier csv
    monF = open("liste.csv", "a", encoding="utf-8")
    monF.write("\n" + log + ";" + Mdp + ";0")
    monF.close
    # Ensuite on lui affiche une page de confirmation d'incription avec le lien vers le quizz
    print('''
            <!DOCTYPE html>
                <html>
                	<head>
                		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
                		<title>Quizz</title>
                		<link rel="stylesheet" type="text/css" href="css/main.css"/>
                        <link rel="icon" type="image/png" href="img/icon.png"/>
                		<script type="text/javascript" src="fonctionJS.js"></script>
                	</head>

                	<body>
                        <div id="content">
      		                <p>Félicitation {} ! Vous êtes inscrit sur notre site ! Vous pouvez commencer à  jouer ou proposer de nouvelles questions au quizz !</p>
                            <form method="POST" action="jeu.py">
                                <input type="hidden" name="login" value="{}"/>
                                <button>Commencer</button>
                            </form>
                            <form method="POST" action="AddQuestions.py">
                                <input type="hidden" name="login" value="{}">
                                <button>Proposer une nouvelle question</button>
                            </form>
                        </div>
                	</body>
                </html>
    '''.format(log, log, log))

else:  # Sinon on lui envoie le(s) message(s) d'erreur(s)
    print('''
        <!DOCTYPE html>

        <html>
        <head>
            <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
            <title>S'INSCRIRE</title>
            <link rel="stylesheet" type="text/css" href="css/main.css"/>
            <link rel="icon" type="image/png" href="img/icon.png"/>
            <script type="text/javascript" src="fonctionJS.js"></script>
        </head>

        <body>
            <div id="content">
                <p>{}{}{}</p> <!--On affiche le(s) message(s) d'erreur-->
                <form id="formulaire" onsubmit="{}" method="POST" action="inscription.py">
                    <label>Login:</label>
                    <br>
                    <input id="login" type="text" name="login" placeholder="Mettez un identifiant" style="border-color:{};" onkeydown="border()" required/>
        			<br><br>
        			<label>Mot de passe:</label>
        			<br>
        			<input id="mdp" type="password" name="mdp" placeholder="Mettez un mot de passe" style="border-color:{};" onkeydown="border2()" required/>
        			<br>
        			<button onclick="verifier()">S'inscrire</button>
        		</form>
            </div>
			<div id="redirection">
				<p>Déjà inscrit ? <a href="authentification.html">Connectez-vous !</a></p>
			</div>
    	</body>
        </html>

        '''.format(msg1, msg2, msg3, submit, borderC1, borderC2))
