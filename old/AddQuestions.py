#! C:\python\python311\python.exe
# -*- coding: utf8 -*-
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html")
print()

donnees=cgi.FieldStorage() #On récupère le nom du joueur
log=donnees.getvalue("login")

#On fait un formulaire pour que le joueur puisse saisir sa question et ses réponses et choisir laquelle est la réponse juste si le joueur est connecteur (si on reçoit son login)
if log!=None: #On fait les test pour savoir si le joueur est connecté
    print('''
            <!DOCTYPE html>

            <html>
            	<head>
            		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
            		<title>Proposer une question</title>
            		<link rel="stylesheet" type="text/css" href="css/main.css"/>
            		<link rel="icon" type="image/png" href="img/icon.png"/>
            		<script type="text/javascript" src="fonctions.js"></script>
            		<style>
            			#content{
            				top:1%;
            				transform:translate(-50%);
            				padding-bottom:15px;
            				padding-top:10px;
            			}
            		</style>
            	</head>''')
    print('''
            	<body>
            		<div id="content">
            			<p style="font-size:20px;">PROPOSEZ VOTRE QUESTION/RÉPONSES</p>
            			<form id="formulaire" method="POST" action="Added.py">
                            <input type="hidden" name="login" value="{}"/>
            				<label>Question :</label>
            				<br>
            				<input autocomplete="off" type="text" name="question" placeholder="Mettez votre question" required/>
            				<br><br>
            				<label>Reponse 1 :</label>
            				<br>
            				<input autocomplete="off" type="text" name="Rep1" placeholder="Mettez votre réponse 1" required/>
            				<br><br>
            				<label>Reponse 2 :</label>
            				<br>
            				<input autocomplete="off" type="text" name="Rep2" placeholder="Mettez votre réponse 2" required/>
            				<br><br>
            				<label>Reponse 3 :</label>
            				<br>
            				<input autocomplete="off" type="text" name="Rep3" placeholder="Mettez votre réponse 3" required/>
            				<br><br>
            				<label>Reponse 4 :</label>
            				<br>
            				<input autocomplete="off" type="text" name="Rep4" placeholder="Mettez votre réponse 4" required/>
            				<br><br>
            				<label for="choixTaille">Choisissez la bonne réponse :</label>
            				<br>
            				<select name="correction">
            					<option value=1>Réponse 1</option>
            					<option value=2>Réponse 2</option>
            					<option value=3>Réponse 3</option>
            					<option value=4>Réponse 4</option>
            				</select>
            				<br>
            				<button>Valider</button>
            			</form>
            		</div>
            	</body>
            </html>
        '''.format(log))

else: #Sinon on affiche une autre page lui demandant de se connecter ou de s'inscrire
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




