#! C:\python\python311\python.exe

class DB:
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
