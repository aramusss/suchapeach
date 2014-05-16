__author__ = 'aram'

import sys
sys.path.insert(0, '../model')
from mobileapp import *

class DbController:
    def __init__(self, pathToDb="../database/database.txt"):
        self.pathToDb = pathToDb

    def insertLine(self, line):
        with open(self.pathToDb, "a") as f:
            f.write(line + "\n")
            print("App added successfully!")

    def getAllApps(self):
        freeAppList = list()
        with open(self.pathToDb, "r") as f:
            for line in f:
                freeAppList.append(line)
        return freeAppList