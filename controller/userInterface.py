__author__ = 'aram'

import sys
sys.path.insert(0, '../model')
from appController import *
from mobileapp import *

while(True):
    print("Hello to Such A Peach App Store!")
    print("How can we help you?")
    print("1 Submit new app: ")
    print("2 View avaliable lists: ")
    print("3 Download an app: ")
    print("4 Comment an app: ")
    print("5 Get app incoming cash from selling: ")
    optionChosen = int(input("Select an option: "))

    appController = AppController()

    if(optionChosen == 1):
        appController.newApp()
    if(optionChosen == 2):
        print("1 View Top Free Apps")
        print("2 View Top Paid Apps")
        optionChosen2 = int(input("Select an option: "))
        appController.listApps(optionChosen2)
    if(optionChosen == 3):
        print("TODO")
    if(optionChosen == 4):
        appName = input("Insert app name: ")
        comment = input("Write comment: ")
        print("TODO")
    if(optionChosen == 5):
        dbController = DbController()
        appUnorderedList = dbController.getAllApps()
        for appString in appUnorderedList:
            name, developer, date, price, numberDownloads, numberScores, score, numberComments = appString.split(";")
            app = MobileApp(name, developer, date, int(price), numberDownloads, numberScores, score, numberComments)
            print (app.getName());
        appName = input("Insert app name: ")
        for appString in appUnorderedList:
            name, developer, date, price, numberDownloads, numberScores, score, numberComments = appString.split(";")
            app = MobileApp(name, developer, date, int(price), numberDownloads, numberScores, score, numberComments)
            if(app.getName() == appName):
                app.calcTotalMoneyEarned()
