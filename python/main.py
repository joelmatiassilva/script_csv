# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import codecs
import json

f = codecs.open('parquimetro.csv',"rb","utf-16")
csvread = csv.reader(f,delimiter=';')
csvread.next()
for row in csvread:
    print row[3]
    # print row[6]
    # data = json.dumps(row[6])
    decoded = json.loads(row[6])
    print decoded["id_token"]
