# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:53:46 2020

@author: Thanasis
"""
import pymysql as sql
import tkinter as tk
from tkinter import ttk

db = sql.connect("127.0.0.1","admin","admin","subscription_manager" )
cur = db.cursor()


    
LARGEFONT =("Verdana", 35) 
   
class tkinterApp(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
          
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (SignUpPage, UserProfilePage): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(SignUpPage) 
   
    # to display the current frame passed as 
    # parameter
    def show_frame(self,cont):
        frame = self.frames[cont] 
        frame.tkraise()
         
         
    def sign_up(self,cont,e1,e2,e3,e4,e5,e6):
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
        frame = self.frames[cont] 
        frame.tkraise()
       
   
# first window frame startpage 
   
class SignUpPage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT) 
          
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
                            command = lambda : controller.sign_up(UserProfilePage,e1=e1,e2=e2,e3=e3,e4=e4,e5=e5,e6=e6))
        button1.grid(row = 6, column = 1, padx = 10, pady = 10)        
        
   
# second window frame page1  
class UserProfilePage(tk.Frame): 
    def __init__(self, parent, controller):         
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="This is the profile bitch", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
       
   
# Driver Code 
app = tkinterApp() 
app.mainloop() 

#data = cur.fetchall()
#print(str(data)[6:19])
db.close()