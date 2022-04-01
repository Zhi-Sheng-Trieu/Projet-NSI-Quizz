#! D:\python\python.exe
# -*- coding: utf8 -*-
from fonction import*
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html")
print()

donneesLogMdp=ouvrir("liste.csv")

donnees=cgi.FieldStorage() #On récupère le texte saisi dans le formulaire
log=donnees.getvalue("login") #On le transforme en chaine de caractères et on l'affecte à des variables
Mdp=donnees.getvalue("mdp")

borderC1=""  #On créer des variabbles vides contenant la couleur du cadre du formulaire
borderC2=""
msg1="" #On créer une variable vide pour le message d'erreur pour le login
msg2="" #On créer une variable vide pour le message d'erreur pour le mdp
submit="return false" #On met par défaut le return en return false
logReprint="" #On fait une variable qui va contenir le login au cas où le joueur n'avait pas saisit le bon mdp pour éviter au joueur de re-saisir son login si il était bon


if log in donneesLogMdp: #On fait des tests pour vérifier si le login et le mdp correspondent à  ceux de la liste
    msg1="" #Si login est bon on s'assure de retirer le message d'erreur et la bordure rouge du login
    borderC1=""
    logReprint=log #Et on fait met à jour la variable au cas où un login était déjà saisit
    if Mdp in donneesLogMdp[log][0]: #Ensuite on fait un test pour le mdp
        submit="return true" #Si lui aussi est correct on met à jour le return et on affiche une page de confirmation redirigeant vers le quizz
        print('''<!DOCTYPE html>

                    <html>
                    	<head>
                    		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
                    		<title>Quizz</title>
                    		<link rel="stylesheet" type="text/css" href="css/Quizz-css.css"/>
                            <link rel="icon" type="image/png" href="img/icon.png"/>
                    		<script type="text/javascript" src="fonctionJS.js"></script>
                    	</head>

                    	<body>
                            <div id="content">
          		                <p>Félicitation {} ! Vous êtes connecté sur notre site ! Vous pouvez commencer à  jouer ou ajouter de nouvelles questions au quizz !</p>
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
        '''.format(log,log,log))
    else:
        msg2="Vous avez saisi le mauvais mot de passe." #Si le mdp est incorrect on revoit un message d'erreur
        borderC2="red" #Et on met la bordure du mdp en rouge

else:
    msg1="Ce login n'existe pas." #Si le login est incorrect on revoit un autre message d'erreur
    borderC1="red"

#Si il y a bien une erreur on ré-affiche le formulaire avec le msg d'erreur

if submit=="return false":
    print('''
    <!DOCTYPE html>

    <html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
        <title>Se connecter</title>
        <link rel="stylesheet" type="text/css" href="css/Quizz-css.css"/>
		<link rel="icon" type="image/png" href="img/icon.png"/>
        <script type="text/javascript" src="fonctionJS.js"></script>
    </head>

    <body>
		<div id="content">
            <p>{}{}</p> <!--On affiche le(s) message(s) d'erreur-->
            <form id="formulaire" onsubmit="{}" method="POST" action="authentification.py">
            <label>Login:</label>
                <br>
                <input id="login" type="text" name="login" placeholder="Mettez votre identifiant" style="border-color:{};" onkeydown="border()" value="{}" required/>
    			<br><br>
    			<label>Mot de passe:</label>
    			<br>
    			<input id="mdp" type="password" name="mdp" placeholder="Mettez votre mot de passe" style="border-color:{};" onkeydown="border2()" required/>
    			<br>
    			<button onclick="verifier()">Se connecter</button>
    		</form>
			<div id="redirection">
				<p>Toujours pas inscrit ? <a href="inscription.html">Inscrivez-vous !</a></p>
			</div>
        </div>
	</body>
    </html>

    '''.format(msg1,msg2,submit,borderC1,logReprint,borderC2))
