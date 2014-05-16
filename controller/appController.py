__author__ = 'aram'

import sys
sys.path.insert(0, '../model')
from mobileapp import *

import datetime

class AppController:

    def newApp(self):
        appName = input("App name: ")
        devName = input("Developer name: ")
        appPrice = input("Price (leave it empty if free): ")
        actualDate = datetime.datetime.now()
        appToInsert = MobileApp(appName, devName, str(actualDate), appPrice, 0, 0, 0, 0)
        appToInsert.insertToDb();

test = AppController()
test.newApp()