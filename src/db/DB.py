import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER')
if USER is None:
    USER =  'root'
PASSWORD = os.getenv('PASSWORD')
if PASSWORD is None:
    PASSWORD = ''
HOST = os.getenv('HOST')
if HOST is None:
    HOST = 'localhost'
DATABASE = os.getenv('DATABASE')
if DATABASE is None:
    DATABASE = 'quizz'

class DB:
    connection = None

    @staticmethod
    def connect():
        
        if DB.connection is None:
            try:
                DB.connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
                print("Connexion à la base de données réussie")
            except mysql.connector.Error as err:
                print("Erreur: {}".format(err))
        else :
            print("Connexion déjà établie")
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
