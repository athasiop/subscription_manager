# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:06:09 2020

@author: Thanasis
"""

import tkinter as tk
from tkinter import ttk
from SignUpPage import SignUpPage
from UserProfilePage import UserProfilePage


class LoginPage(tk.Frame):
    user_info ={}
    frames = {}
    def __init__(self,parent,cur,user_info,frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.user_info=user_info
        self.frames = frames
        
        tk.Label(self,text = "Enter Your Username").grid(row=0,column=0)
        entry_username = tk.Entry(self)
        entry_username.grid(row=0,column=1)
        
        tk.Label(self,text = "Enter Your Email").grid(row=1,column=0)
        entry_email = tk.Entry(self)
        entry_email.grid(row=1,column=1)
        
        login_button = ttk.Button(self,text="Log In",command=lambda:self.login(str(entry_username.get()),str(entry_email.get())))
        login_button.grid(row=2,column=0)
        
        sign_up_button = ttk.Button(self,text="Sign Up",command = lambda:self.sign_up())
        sign_up_button.grid(row=2,column=1)
    def login(self,username,email):
        try:
            instr = "SELECT * FROM user WHERE user_name='"+username+"' AND email='"+email+"'"
            self.cur.execute(instr)
            record = self.cur.fetchone()        
            self.user_info["user_name"] =  record[1]
            self.user_info["birth_date"] =  record[2]
            self.user_info["email"] =  record[4]
            self.user_info["country"] =  record[5]
            self.user_info["zip_code"] =  record[6]
            self.user_info["street"] =  record[7]
            #TODO add age
            
            frame = self.frames[UserProfilePage]
            frame.UpdateProfile(self.user_info)
            frame.tkraise()
        except:
            tk.Label(self,text="User Not Found",bg="red").grid(row=3,column=0)
            print("User Not Found!")
    def sign_up(self):
        frame = self.frames[SignUpPage]
        frame.tkraise()