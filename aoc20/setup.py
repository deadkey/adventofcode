import sys, time, os
from datetime import date

def get_day(): return date.today().day
def get_year(): return date.today().year

def createfolders(DAY):
    dirname = 'D{}'.format(DAY)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        open("{}/1.in".format(dirname), "w+")
        open("{}/2.in".format(dirname), "w+")
        open("{}/3.in".format(dirname), "w+")
        with open("{}/d{}.py".format(dirname, DAY), "w+") as f:
            f.write(open("template.py").read())
        
day = get_day()
createfolders(day)

