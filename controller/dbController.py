__author__ = 'aram'

import sys
sys.path.insert(0, '../model')
from mobileapp import *

class DbController:
    def __init__(self, pathToDb="../database/database.txt"):
        self.pathToDb = pathToDb

    def insertLine(self, line):
        with open(self.pathToDb, "a") as f:
            f.write(line)
            print("App added successfully!")
