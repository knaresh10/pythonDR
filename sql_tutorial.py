# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:10:27 2022

@author: Naresh
"""

#pip install mysql-connector-python
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "121310Besties@",
    database = "naresh"
    )

#print(db)

#to create databases

cur = db.cursor()

#to create a database
#cur.execute("CREATE DATABASE naresh")
"""
studenttable = '''CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )'''

cur.execute(studenttable)

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Ram", "CSE", "85", "B", "19") 



cur.execute(sql, val) """

q = "select * from student"

cur.execute(q)

result = cur.fetchall()

for i in result:
    print(i)

#db.commit()
db.close()