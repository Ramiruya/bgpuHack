import requests
import json
import srat

class Teacher:
    def __init__(self, fio):
        self.FIO = fio
        self.titles = []
    
    def loadTitles(self):
        titles = srat.getName()
        self.titles = titles

teach1 = Teacher('Иванов Иван Иванович')
teach1.loadTitles()
print(teach1.FIO, teach1.titles)