from tkinter import *
from tkinter import messagebox
import mysql.connector




def fun():
    def dataentry():
        
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
        
    def clear_button():
        m.destroy()

    
    m = Tk()
    m.geometry("250x300")

    Label(m, text = "Name").grid(row = 0)
    e1 = Entry(m) 
    e1.focus_set()
    e1.grid(row = 0, column = 1)
    Label(m, text = "Roll Number").grid(row = 1)
    e2 = Entry(m)
    e2.grid(row = 1, column = 1)

    Label(m, text = "branch").grid(row = 2)
    e3 = Entry(m)
    e3.grid(row = 2, column = 1)

    Label(m, text = "college").grid(row = 3)
    e4 = Entry(m)
    e4.grid(row = 3, column = 1)

    Label(m, text = "phone no").grid(row = 4)
    e5 = Entry(m)
    e5.grid(row = 4, column = 1)

    Label(m, text = "age").grid(row = 5)
    e6 = Entry(m)
    e6.grid(row = 5, column = 1)

    b1 = Button(m, text = "submit", command = lambda : [dataentry(), clear_button()]).grid(row = 6, column = 1)
    m.mainloop() 


root = Tk()

root.geometry("200x200")


b1 = Button(root, text = "insert", command = fun)
b1.pack()
#b1.place(relx = 0.5, rely = 0.35, anchor = 'center')
b2 = Button(root, text = "show")
b2.pack()
#b2.place(relx = 0.5, rely = 0.56, anchor = 'center')

root.mainloop()

