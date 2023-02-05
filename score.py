#! C:\python\python311\python.exe
# -*- coding: utf8 -*-
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html")
print()

donnees=cgi.FieldStorage() #On récupère le texte saisi dans le formulaire
rep1=donnees.getvalue("Rep1") #On récupère les valeurs des réponses du joueurs
rep2=donnees.getvalue("Rep2")
rep3=donnees.getvalue("Rep3")
rep4=donnees.getvalue("Rep4")
k1=donnees.getvalue("Q1") #On récupère les clés des questions
k2=donnees.getvalue("Q2")
k3=donnees.getvalue("Q3")
k4=donnees.getvalue("Q4")
log=donnees.getvalue("login") #On récupère l'identifiant du joueur
score=0


#On affiche la page html avec le score fait par le joueur et son score total
if log!=None: #On fait les test pour savoir si le joueur est connecté
    monF=open("liste.csv", "r", encoding="utf-8") #On ouvre le fichier contenant les donnees des joueurs
    monF.readline()
    donneesPlayer={}
    for lig in monF:    #On parcourt ligne par ligne le fichier
        lig=lig.rstrip("\n") #On retire le retour a la ligne
        vals=lig.split(";") #On retire les ";"
        donneesPlayer[vals[0]]=vals[1],vals[2]  #On met à jour le dictionnaire
    monF.close() #On ferme le fichier

    mesQ=open("questions.csv", "r", encoding="utf-8") #On ouvre le fichier contenant les questions
    mesQ.readline()
    Q={}
    for lig in mesQ:    #On parcourt ligne par ligne le fichier
        lig=lig.rstrip("\n") #On retire le retour a la ligne
        vals=lig.split(";") #On retire les ";"
        Q[vals[0]]=vals[1],vals[2],vals[3],vals[4],vals[5],vals[6] #On ajoute les questions et leurs reponses au dictionnaire
    mesQ.close() #On ferme le fichier

    quest1=Q[k1]  #On retrouve les questions posées au joueur pour faire un correction
    quest2=Q[k2]
    quest3=Q[k3]
    quest4=Q[k4]
    rep=[rep1,rep2,rep3,rep4]  #On fait une liste des valeurs des réponses du joueurs
    R=[quest1,quest2,quest3,quest4] #On fait une liste des variables contenant les questions/réponses et les valeur des réponses justes

    for i in range(4): #On fait une boucle pour parcourir chaque réponse
        if rep[i-1]==R[i-1][5]: #On regarde si chaque réponse est juste
            score+=3 #Si oui on augmente le score
        else:
            score-=1 #Sinon on le diminue

    scoreJoueur=int(donneesPlayer[log][1]) #On récupère le score du joueur

    scoreJoueur+=score #On le met à jour le score du joueur

    donneesPlayer[log]=str(donneesPlayer[log][0]),str(scoreJoueur) #On le met à jour le score du joueur dans le dictionnaire

    donneesScores=[]
    monF=open("liste.csv", "w", encoding="utf-8") #On met à jour le score du joueur dans le fichier
    monF.write("login;mdp;score")
    for key in donneesPlayer:
        monF.write("\n"+str(key)+";"+donneesPlayer[key][0]+";"+donneesPlayer[key][1])
        donneesScores.append([int(donneesPlayer[key][1]),key]) #On garde dans la liste donneesScores le score des joueurs et leur nom pourle classement
    monF.close()

    L=[]
    for j in range(len(donneesScores)): #On fait le classement en fonction du score des joueurs les triant dans une liste L
        maxi=max(donneesScores)
        donneesScores.remove(maxi)
        L.append(maxi)
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
                    <div id="quizz">
    	                <p>Vous avez fait un scrore de {}/12 ! Votre score total est de {}</p>'''.format(score,scoreJoueur))

    print('''
                        <div class="classement">
                    		<p>Classement :</p>
                            <ol>''')
    for k in range(len(L)):
        print('''<li>{} : {} pt</li>'''.format(L[k][1],L[k][0]))


    print('''
                            </ol>
                        </div>
    	                <p>Correction :</p>''')

    for c in range(4):
        print('''<p>Question {} : {}</p>
                    <p>Réponse juste : {}</p><br>
        '''.format(c+1,R[c-1][0],R[c-1][int(R[c-1][5])]))



    print('''                    <form method="POST" action="jeu.py">
                            <input type="hidden" name="login" value="{}">
                            <button>Nouvelle partie</button>
                        </form>
                        <br>
                        <form method="POST" action="AddQuestions.py">
                            <input type="hidden" name="login" value="{}">
                            <button>Proposer une nouvelle question</button>
                        </form>
                    </div>


            	</body>
            </html>
    '''.format(log,log))

else: #Sinon on affiche une autre page lui demandant de se connecter ou de s'inscrire
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


