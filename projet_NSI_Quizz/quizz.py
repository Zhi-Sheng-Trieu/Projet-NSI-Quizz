#! D:\python\python.exe
# -*- coding: utf8 -*-
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html")
print()


class db:
    def ouvrir(self,F):
        monF=open(F, "r", encoding="utf-8")
        monF.readline()
        donnees={}
        for lig in monF:    #On parcourt ligne par ligne le fichier
            lig=lig.rstrip("\n") #On retire le retour a la ligne
            vals=lig.split(";") #On retire les ","
            donnees[vals[0]]=vals[1],vals[2]
        monF.close() #On ferme le fichier
        return donnees




