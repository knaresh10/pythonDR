import mysql.connector
import tkinter as tk
from tkinter import messagebox

#function to read data from entries and store it in database
def fun():
        
    name = e1.get()
    roll = e2.get()
    branch = e3.get()
    col = e4.get()
    ph = e5.get()
    age = e6.get()
    #print(name,roll,branch,col,ph,age)
    if not name or not roll or not branch or not col or not ph or not age:
        messagebox.showinfo("empty",'some fields are empty')
        return
    #to connect to database
    db = mysql.connector.connect (
            host = "localhost",
            user = "root",
            passwd = "121310Besties@",
            database = "tests"
        )
    
    cur = db.cursor()
    
    sql = "INSERT INTO student(name, roll, branch, college, ph, age)\
        VALUES(%s, %s, %s, %s, %s, %s)"
    val = (name, roll, branch, col, ph, age)
    
    try:
        cur.execute(sql, val)
        messagebox.showinfo("insertion", "successfully inserted the data")
        
    except:
        messagebox.showinfo("DUPLICATES","student with same roll no is already present")  
        
    db.commit() 
    db.close()
    
#to clear data after submit button
def clear_button():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')

    e1.focus_set()


#__main___

m = tk.Tk()
m.geometry("250x300")

tk.Label(m, text = "Name").grid(row = 0)
e1 = tk.Entry(m) 
e1.focus_set()
e1.grid(row = 0, column = 1)
tk.Label(m, text = "Roll Number").grid(row = 1)
e2 = tk.Entry(m)
e2.grid(row = 1, column = 1)

tk.Label(m, text = "branch").grid(row = 2)
e3 = tk.Entry(m)
e3.grid(row = 2, column = 1)

tk.Label(m, text = "college").grid(row = 3)
e4 = tk.Entry(m)
e4.grid(row = 3, column = 1)

tk.Label(m, text = "phone no").grid(row = 4)
e5 = tk.Entry(m)
e5.grid(row = 4, column = 1)

tk.Label(m, text = "age").grid(row = 5)
e6 = tk.Entry(m)
e6.grid(row = 5, column = 1)

b1 = tk.Button(m, text = "submit", command = lambda : [fun(), clear_button()]).grid(row = 6, column = 1)

m.mainloop() 
