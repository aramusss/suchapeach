__author__ = 'aram'

import sys
import os

sys.path.insert(0, '../model')
from mobileapp import *
from dbController import *

import datetime

class AppController:

    def newApp(self):
        appName = input("App name: ")
        devName = input("Developer name: ")
        appPrice = input("Price (leave it empty if free): ")
        actualDate = datetime.datetime.now()
        appToInsert = MobileApp(appName, devName, str(actualDate), appPrice, 0, 0, 0, 0)
        appToInsert.insertToDb();

    def listApps(self, type):
        print("Listing Apps ordered by our ranking...")
        dbController = DbController()
        appUnorderedList = dbController.getAllApps()
        appOrderedList = list()
        for appString in appUnorderedList:
            name, developer, date, price, numberDownloads, numberScores, score, numberComments = appString.split(";")
            app = MobileApp(name, developer, date, int(price), numberDownloads, numberScores, score, numberComments)
            if type == 0:
                if app.getPrice() == 0:
                    appScore = ((float(app.getNumberDownloads()) * 0.6) + (float(app.getScore()) * 0.25) + (float(app.getNumberComments()) * 0.15))
                    appToList = (app, appScore)
                    appOrderedList.append(appToList)
            elif type == 1:
                if app.getPrice() > 0:
                    appScore = ((float(app.getNumberDownloads()) * 0.6) + (float(app.getScore()) * 0.25) + (float(app.getNumberComments()) * 0.15))
                    appToList = (app, appScore)
                    appOrderedList.append(appToList)
            else:
                print("Internal error. You should not be here.")
        self.printOrderedList(appOrderedList)

    def printOrderedList(self, orderedList):
        maxScore = 0;
        for app in orderedList:
            if app[1] > maxScore:
                maxScore = app[1]
        for app in orderedList:
            if app[1] == maxScore:
                print(app[0].getName() + " with score " + str(app[1]))
                orderedList.remove(app)
        if orderedList:
            self.printOrderedList(orderedList)

    #CODE FUNCTION FROM ADRIA BIARNES
    def sumarDescarga(self, nombre, pathToDb="../database/database.txt"):
        """Suma una descarga a la aplicación con ese nombre. Devuelve True o False en funcion de si se ha encontrado (y modificado) o no"""
        if os.path.isfile(pathToDb):
            file = open(pathToDb, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(pathToDb, 'w') as file:
                for linia in llista:
                    if linia.split(";")[0] != nombre:
                        file.write(linia)
                    else:
                        linia1 = linia.split(";")
                        descargues = int(linia.split(";")[4])
                        resultat = linia1[0]+";"+linia1[1]+";"+linia1[2]+";"+linia1[3]+";"+str(descargues+1)+";"+linia1[5]+";"+linia1[6]+";"+linia1[7]
                        file.write(resultat)
                        trobat = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")
        return trobat
    #CODE FUNCTION FROM ADRIA BIARNES
    def sumarComentario(self, nombre,  pathToDb="../database/database.txt"):
        """Suma un comentario a la aplicación con ese nombre. Devuelve True o False en funcion de si se ha encontrado (y modificado) o no"""
        if os.path.isfile(pathToDb):
            file = open(pathToDb, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(pathToDb, 'w') as file:
                for linia in llista:
                    if linia.split(";")[0] != nombre:
                        file.write(linia)
                    else:
                        linia1 = linia.split(";")
                        comentarios = linia.split(";")[7]
                        comentarios = int(comentarios)
                        resultat = linia1[0]+";"+linia1[1]+";"+linia1[2]+";"+linia1[3]+";"+linia1[4]+";"+linia1[5]+";"+linia1[6]+";"+str(comentarios+1)+"\n"
                        file.write(resultat)
                        trobat = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")
        return trobat

test = AppController()
test.listApps(1)