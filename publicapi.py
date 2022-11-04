import requests
import json
import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='publicapidb')
except mysql.connector.Error as e:
    sys.exit("connection error")
mycursor=mydb.cursor()
data=requests.get("https://api.publicapis.org/entries").text
data_info=json.loads(data)
for i in data_info['entries']:
    try:
        sql="INSERT INTO `publicapidata`( `api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data=(i['API'],i['Description'],i['Auth'],i['HTTPS'],i['Cors'],i['Link'],i['Category'])
        mycursor.execute(sql,data)
        mydb.commit()
    except mysql.connector.Error as e:
        print("Error",e)
        print("data inserted successfully,",i['API'])      