# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:53:46 2020

@author: Thanasis
"""
import pymysql as sql
import tkinter as tk
from SignUpPage import SignUpPage
from LoginPage import LoginPage
from UserProfilePage import UserProfilePage

user_info = {
    "user_name":"",
    "birth_date":"",
    "email":"",
    "country":"",
    "zip_code":"",
    "street":""
    }

db = sql.connect("127.0.0.1","admin","admin","subscription_manager" )
cur = db.cursor()


   
LARGEFONT =("Verdana", 35) 
   
class tkinterApp(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self):  
         
        # __init__ function for class Tk 
        tk.Tk.__init__(self) 
          
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        # initializing frames to an empty array 
        self.frames = {}   
        self.frames[SignUpPage] = SignUpPage(container,cur,db,user_info,self.frames)
        self.frames[SignUpPage].grid(row=0,column=0,sticky="nsew")
        self.frames[UserProfilePage] = UserProfilePage(container,user_info)
        self.frames[UserProfilePage].grid(row=0,column=0,sticky="nsew")
        self.frames[LoginPage] = LoginPage(container,cur,user_info,self.frames)
        self.frames[LoginPage].grid(row=0,column=0,sticky="nsew")
        # iterating through a tuple consisting 
        # of the different page layouts
        
        
        self.show_frame(LoginPage) 
   
    # to display the current frame passed as 
    # parameter
    def show_frame(self,cont):
        frame = self.frames[cont] 
        frame.tkraise()
         
         
    
    
    
# first window frame startpage 
   

   
# second window frame page1  

# Driver Code 

app = tkinterApp() 
app.mainloop() 


db.close()