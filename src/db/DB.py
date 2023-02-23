import mysql.connector


class DB:
    config = ""
    connection = None

    @staticmethod
    def setConfig(config):
        DB.config = config
        DB.connection = None

    @staticmethod
    def connect():
        if DB.connection is None:
            try:
                DB.connection = mysql.connector.connect(host='localhost',
                                                        database='quizz',
                                                        user='root',
                                                        password='')
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
