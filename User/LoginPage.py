# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:13:33 2020

@author: Thanasis
"""
import tkinter as tk
from tkinter import ttk

class LoginPage(tk.Frame):
    
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
            self.user_info["user_id"]=record[0]
            self.user_info["user_name"] =  record[1]
            self.user_info["birth_date"] =  record[2]
            self.user_info["email"] =  record[4]
            self.user_info["country"] =  record[5]
            self.user_info["zip_code"] =  record[6]
            self.user_info["street"] =  record[7]
            #TODO add age
            
            frame = self.frames["UserProfilePage"]
            frame.UpdateProfile()
            frame.show()
            frame.tkraise()
        except tk.TclError as e:
            print("Issue with tinker: "+str(e))
        except TypeError as e:
            self.user_not_found_label = tk.Label(self,text="User Not Found",bg="red")
            self.user_not_found_label.grid(row=3,column=0)
            self.after(3000, self.clear_label)
            print("Error: "+str(e))
    def clear_label(self):
        self.user_not_found_label.grid_forget()
    def sign_up(self):
        frame = self.frames["SignUpPage"]
        frame.tkraise()    