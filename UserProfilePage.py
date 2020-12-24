# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:14:43 2020

@author: Thanasis
"""
import tkinter as tk

class UserProfilePage(tk.Frame):
    user_info = {}
    def __init__(self, parent,user_info):         
        tk.Frame.__init__(self, parent)        
        #self.user_info = user_info
        tk.Label(self,text="Username = ").grid(row=0,column=0)
        
        tk.Label(self,text="Birth Date").grid(row=1)
        tk.Label(self,text="Email = ").grid(row=2)
        tk.Label(self,text="Country = ").grid(row=3)
        tk.Label(self,text="Zip Code = ").grid(row=4)
        tk.Label(self,text="Street = ").grid(row=5)
    def UpdateProfile(self,user_info):                 
        self.user_info = user_info
        print(user_info)
        tk.Label(self,text=user_info["user_name"]).grid(row=0,column=1)
        tk.Label(self,text=user_info["birth_date"]).grid(row=1,column=1)
        tk.Label(self,text=user_info["email"]).grid(row=2,column=1)
        tk.Label(self,text=user_info["country"]).grid(row=3,column=1)
        tk.Label(self,text=user_info["zip_code"]).grid(row=4,column=1)
        tk.Label(self,text=user_info["street"]).grid(row=5,column=1)