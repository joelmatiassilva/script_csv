# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import codecs
import json
import os, errno

path1 = "./files"
if not os.path.exists(path1):
    os.makedirs(path1)
f = codecs.open('parquimetro.csv',"rb","utf-16")
csvread = csv.reader(f,delimiter=';')
csvread.next()
for row in csvread:
    print row[3]
    decoded = json.loads(row[6])
    print "id_tokenn: " + decoded["id_token"]
    print "reresh_token: " + decoded["refresh_token"]
    file = open("files/"+ row[3] + "_token.json", "w")
    file.write("{\"api_token_id\":\"" + decoded["id_token"] + "\", \"api_token_renew\":\"" + decoded["refresh_token"] +"\"}")
