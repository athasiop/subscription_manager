# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:53:46 2020

@author: Thanasis
"""
import pymysql as sql
import tkinter as tk

db = sql.connect("127.0.0.1","admin","admin","subscription_manager" )
cur = db.cursor()

def confirm_input():
    user_name = str(e1.get())
    birth_date = str(e2.get())
    email = str(e3.get())
    country = str(e4.get())
    zip_code = str(e5.get())
    street = str(e6.get())
      
    instr = "INSERT INTO user (user_name,email,country,birth_date,zip_code,street) VALUES ('"+user_name+"','"+email+"','"+country+"','"+birth_date+"','"+zip_code+"','"+street+"')"
    print(instr)
    cur.execute(instr)
    db.commit()


root = tk.Tk()
tk.Label(root,text="Username").grid(row=0)
tk.Label(root,text="Birth Date").grid(row=1)
tk.Label(root,text="Email").grid(row=2)
tk.Label(root,text="Country").grid(row=3)
tk.Label(root,text="Zip Code").grid(row=4)
tk.Label(root,text="Street").grid(row=5)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)
e6 = tk.Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)

tk.Button(root,text="Confirm",command=confirm_input).grid(row=7)

tk.mainloop()

#data = cur.fetchall()
#print(str(data)[6:19])
db.close()