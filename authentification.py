#! C:\python\python311\python.exe
# -*- coding: utf8 -*-
import cgi
import cgitb
from src.db.DB import DB
from src.render.Renderer import Renderer

cgitb.enable()
print("Content-type:text/html")
print()

donneesLogMdp = DB.ouvrir("liste.csv")

donnees = cgi.FieldStorage()  # On recupere le texte saisi dans le formulaire
log = donnees.getvalue("login")  # On le transforme en chaine de caracteres et on l'affecte a des variables
Mdp = donnees.getvalue("mdp")

borderC1 = ""  # On creer des variabbles vides contenant la couleur du cadre du formulaire
borderC2 = ""
msg1 = ""  # On creer une variable vide pour le message d'erreur pour le login
msg2 = ""  # On creer une variable vide pour le message d'erreur pour le mdp
submit = "return false"  # On met par defaut le return en return false
logReprint = ""  # On fait une variable qui va contenir le login au cas où le joueur n'avait pas saisit le bon mdp pour eviter au joueur de re-saisir son login si il etait bon
print(Renderer.get_header())

if log in donneesLogMdp:  # On fait des tests pour verifier si le login et le mdp correspondent a ceux de la liste
    msg1 = ""  # Si login est bon on s'assure de retirer le message d'erreur et la bordure rouge du login
    borderC1 = ""
    logReprint = log  # Et on fait met a jour la variable au cas où un login etait deja saisit
    if Mdp in donneesLogMdp[log][0]:  # Ensuite on fait un test pour le mdp
        submit = "return true"  # Si lui aussi est correct on met a jour le return et on affiche une page de confirmation redirigeant vers le quizz
        print('''
                            <div id="content">
          		                <p>Felicitation {} ! Vous êtes connecte sur notre site ! Vous pouvez commencer a jouer ou ajouter de nouvelles questions au quizz !</p>
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
    else:
        msg2 = "Vous avez saisi le mauvais mot de passe."  # Si le mdp est incorrect on revoit un message d'erreur
        borderC2 = "red"  # Et on met la bordure du mdp en rouge

else:
    msg1 = "Ce login n'existe pas."  # Si le login est incorrect on revoit un autre message d'erreur
    borderC1 = "red"

# Si il y a bien une erreur on re-affiche le formulaire avec le msg d'erreur

if submit == "return false":
    print('''
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

    '''.format(msg1, msg2, submit, borderC1, logReprint, borderC2))
