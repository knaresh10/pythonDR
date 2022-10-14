# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:50:07 2022

@author: Naresh
"""
import mysql.connector



def fun():
    name = t1.get()
    branch = t2.get()
    roll = t3.get()
    sec = t4.get()
    age = t5.get()
    
    
    db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "121310Besties@",
            database = "naresh"
        )

    cur = db.cursor() 
    
    sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
    VALUES (%s, %s, %s, %s, %s)"
    val = (name, branch, roll, sec, age)
    
    
    cur.execute(sql, val)
    db.commit()
    
    db.close()
    
import tkinter as tk;

r = tk.Tk()

r.geometry('200x150')

t1 = tk.Entry(r)
t2 = tk.Entry(r)
t3 = tk.Entry(r)
t4 = tk.Entry(r)
t5 = tk.Entry(r)

b1 = tk.Button(r, text = 'Submit' , command = fun)

t1.pack()
t2.pack()
t3.pack()
t4.pack()
t5.pack()
b1.pack()
r.mainloop()


