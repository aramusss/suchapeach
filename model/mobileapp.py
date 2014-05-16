__author__ = 'aram'

import sys
sys.path.insert(0, '../controller')
from dbController import *

class MobileApp:
    def __init__(self, name, developer, date, price, numberDownloads, numberScores, score, numberComments):
        self.name = name
        self.developer = developer
        self.date = date
        if price == '':
            self.price = 0
        else:
            self.price = price
        self.numberDownloads = numberDownloads
        self.numberScores = numberScores
        self.score = score
        self.numberComments = numberComments

    def getName(self):
        return self.name
    def getDeveloper(self):
        return self.developer
    def getDate(self):
        return self.date
    def getPrice(self):
        return self.price
    def getNumberDownloads(self):
        return self.numberDownloads
    def getNumberScores(self):
        return self.numberScores
    def getScore(self):
        return self.score
    def getNumberComments(self):
        return self.numberComments

    def insertToDb(self):
        appLine = self.name + ";" + self.developer + ";" + self.date + ";" + str(self.price) + ";" + str(self.numberDownloads) + ";" + str(self.numberScores) + ";" + str(self.score) + ";" + str(self.numberComments)
        database = DbController()
        database.insertLine(appLine)
