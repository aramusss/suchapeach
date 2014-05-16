__author__ = 'aram'

import sys

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


test = AppController()
test.listApps(1)