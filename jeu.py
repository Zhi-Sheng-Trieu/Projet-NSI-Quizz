#! D:\python\python.exe
# -*- coding: utf8 -*-
from random import randint
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html")
print()

donnees=cgi.FieldStorage()
log=donnees.getvalue("login")

#On affiche le quizz avec les questions/réponses
if log!=None: #On fait les test pour savoir si le joueur est connecté
    mesQ=open("questions.csv", "r", encoding="utf-8") #On ouvre le fichier contenant les questions
    mesQ.readline()
    Q={}
    for lig in mesQ:    #On parcourt ligne par ligne le fichier
        lig=lig.rstrip("\n") #On retire le retour a la ligne
        vals=lig.split(";") #On retire les ";"
        Q[vals[0]]=vals[1],vals[2],vals[3],vals[4],vals[5],vals[6] #On ajoute les questions et leurs reponses au dictionnaire
    mesQ.close() #On ferme le fichier

    #On définit les questions aléatoires
    k1=randint(1,len(Q))
    quest1=Q[str(k1)]

    k2=randint(1,len(Q))
    while k1==k2:
        k2=randint(1,len(Q))
    quest2=Q[str(k2)]

    k3=randint(1,len(Q))
    while k1==k3 or k3==k2:
        k3=randint(1,len(Q))
    quest3=Q[str(k3)]

    k4=randint(1,len(Q))
    while k1==k4 or k4==k2 or k4==k3:
        k4=randint(1,len(Q))
    quest4=Q[str(k4)]

    print('''
            <!DOCTYPE html>

            <html>
            	<head>
            		<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
            		<title>Quizz</title>
            		<link rel="stylesheet" type="text/css" href="css/Quizz-css.css"/>
            		<link rel="icon" type="image/png" href="img/icon.png"/>
            		<script type="text/javascript" src="fonctionJS.js"></script>
            	</head>

            	<body>
                    <audio src="audio/Dark_Mystery.mp3" type="audio/mpeg" loop=-1 autoplay></audio>
            		<div id="quizz">
                        <p>Salut {} ! Ce quizz comporte 4 questions. Chaque bonne réponse te donnera 3 points, une mauvaise t'en fera perdre 1.</p>
            			<form id="formulaire" method="POST" action="score.py">
                            <input type="hidden" name="login" value="{}">'''.format(log,log),'''

                <!--Question 1----------------------------------------->
                            <input type="hidden" name="Q1" value="{}">
            				<label for="Question1">{} :</label>
            				<br><br>
            				<input type="radio" id="Q1Rep1" name="Rep1" value="1"/>
            				<label for="Q1Rep1">{}</label>
            				<br><br>
            				<input type="radio" id="Q1Rep2" name="Rep1" value="2"/>
            				<label for="Q1Rep2">{}</label>
            				<br><br>
            				<input type="radio" id="Q1Rep3" name="Rep1" value="3"/>
            				<label for="Q1Rep3">{}</label>
            				<br><br>
            				<input type="radio" id="Q1Rep4" name="Rep1" value="4"/>
            				<label for="Q1Rep4">{}</label>
            				<br><br><br>'''.format(k1,quest1[0],quest1[1],quest1[2],quest1[3],quest1[4]),'''

            				<!--Question 2----------------------------------------->
                            <input type="hidden" name="Q2" value="{}">
            				<label for="Question2">{} :</label>
            				<br><br>
            				<input type="radio" id="Q2Rep1" name="Rep2" value="1"/>
            				<label for="Q2Rep1">{}</label>
            				<br><br>
            				<input type="radio" id="Q2Rep2" name="Rep2" value="2"/>
            				<label for="Q2Rep2">{}</label>
            				<br><br>
            				<input type="radio" id="Q2Rep3" name="Rep2" value="3"/>
            				<label for="Q2Rep3">{}</label>
            				<br><br>
            				<input type="radio" id="Q2Rep4" name="Rep2" value="4"/>
            				<label for="Q2Rep4">{}</label>
            				<br><br><br>'''.format(k2,quest2[0],quest2[1],quest2[2],quest2[3],quest2[4]),'''

            				<!--Question 3----------------------------------------->
                            <input type="hidden" name="Q3" value="{}">
            				<label for="Question3">{} :</label>
            				<br><br>
            				<input type="radio" id="Q3Rep1" name="Rep3" value="1"/>
            				<label for="Q3Rep1">{}</label>
            				<br><br>
            				<input type="radio" id="Q3Rep2" name="Rep3" value="2"/>
            				<label for="Q3Rep2">{}</label>
            				<br><br>
            				<input type="radio" id="Q3Rep3" name="Rep3" value="3"/>
            				<label for="Q3Rep3">{}</label>
            				<br><br>
            				<input type="radio" id="Q3Rep4" name="Rep3" value="4"/>
            				<label for="Q3Rep4">{}</label>
            				<br><br><br>'''.format(k3,quest3[0],quest3[1],quest3[2],quest3[3],quest3[4]),'''

            				<!--Question 4----------------------------------------->
                            <input type="hidden" name="Q4" value="{}">
            				<label for="Question4">{} :</label>
            				<br><br>
            				<input type="radio" id="Q4Rep1" name="Rep4" value="1"/>
            				<label for="Q4Rep1">{}</label>
            				<br><br>
            				<input type="radio" id="Q4Rep2" name="Rep4" value="2"/>
            				<label for="Q4Rep2">{}</label>
            				<br><br>
            				<input type="radio" id="Q4Rep3" name="Rep4" value="3"/>
            				<label for="Q4Rep3">{}</label>
            				<br><br>
            				<input type="radio" id="Q4Rep4" name="Rep4" value="4"/>
            				<label for="Q4Rep4">{}</label>
            				<br><br>'''.format(k4,quest4[0],quest4[1],quest4[2],quest4[3],quest4[4]),'''

            				<button>Valider</button>
            			</form>
            		</div>
            	</body>
            </html>
    ''')
else: #Sinon on affiche une autre page lui demandant de se connecter ou de s'inscrire
    print('''
            <!DOCTYPE html>
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
                			<p>Salut !</p>
                			<p><em>Pour pouvoir <mark>jouer</mark> il faut être <strong>inscrit</strong> !</em></p>
                			<form method="POST" action="inscription.html">
                				<button>S'inscrire</button>
                			</form>
                			<form method="POST" action="authentification.html">
                				<button>Se connecter</button>
                			</form>
                		</div>
                	</body>
                </html>
    ''')
