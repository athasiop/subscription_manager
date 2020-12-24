# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:53:06 2020

@author: Thanasis
"""

import tkinter as tk
from tkinter import ttk
from UserProfilePage import UserProfilePage

class SignUpPage(tk.Frame):
    user_info = {}
    frames = {}
    def __init__(self, parent,cur,db,user_info,frames):  
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.db = db
        self.user_info = user_info
        self.frames = frames
        # label of frame Layout 2 
        label = ttk.Label(self, text ="Sign Up Page") 
          
        # putting the grid in its place by using 
        # grid 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
        tk.Label(self,text="Username").grid(row=0)
        tk.Label(self,text="Birth Date").grid(row=1)
        tk.Label(self,text="Email").grid(row=2)
        tk.Label(self,text="Country").grid(row=3)
        tk.Label(self,text="Zip Code").grid(row=4)
        tk.Label(self,text="Street").grid(row=5)
        
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)
        e6 = tk.Entry(self)
        
        e1.grid(row=0,column=1)
        e2.grid(row=1,column=1)
        e3.grid(row=2,column=1)
        e4.grid(row=3,column=1)
        e5.grid(row=4,column=1)
        e6.grid(row=5,column=1)
        
       
    
        button1 = ttk.Button(self, text ="Sign Up", 
                            command = lambda : self.sign_up(e1=e1,e2=e2,e3=e3,e4=e4,e5=e5,e6=e6))
        button1.grid(row = 6, column = 1, padx = 10, pady = 10)        
    def sign_up(self,e1,e2,e3,e4,e5,e6):
        self.user_info["user_name"] = str(e1.get())
        self.user_info["birth_date"] = str(e2.get())
        self.user_info["email"] = str(e3.get())
        self.user_info["country"] = str(e4.get())
        self.user_info["zip_code"] = str(e5.get())
        self.user_info["street"] = str(e6.get())
       
        instr = "INSERT INTO user (user_name,email,country,birth_date,zip_code,street) VALUES ('"+self.user_info.get("user_name")+"','"+self.user_info.get("email")+"','"+self.user_info.get("country")+"','"+self.user_info.get("birth_date")+"','"+ self.user_info.get("zip_code")+"','"+self.user_info.get("street")+"')"
        print(instr)
        try:
            self.cur.execute(instr)
            self.db.commit()        
            frame = self.frames[UserProfilePage]
            frame.UpdateProfile(self.user_info)
            frame.tkraise()
        except:
            print("invalid input")