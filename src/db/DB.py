import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER', 'root')
PASSWORD = os.getenv('PASSWORD', '')
HOST = os.getenv('HOST', 'localhost')
DATABASE = os.getenv('DATABASE', 'quizz')

class DB:
    connection = None

    @staticmethod
    def connect():
        if DB.connection :
            print("Connexion déjà établie")
        else:
            try:
                DB.connection = DB.connection or mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
                print("Connexion à la base de données réussie")
            except mysql.connector.Error as err:
                print("Erreur: {}".format(err))
        return DB.connection

    @staticmethod
    def ouvrir(nom_fichier):
        monF = open(nom_fichier, "r", encoding="utf-8")
        monF.readline()
        donnees = {}
        for lig in monF:  # On parcourt ligne par ligne le fichier
            lig = lig.rstrip("\n")  # On retire le retour a la ligne
            vals = lig.split(";")  # On retire les ","
            donnees[vals[0]] = vals[1], vals[2]
        monF.close()  # On ferme le fichier
        return donnees
