# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:53:46 2020

@author: Thanasis
"""
import pymysql as sql
import tkinter as tk
from tkinter import ttk

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
        self.frames[UserProfilePage] = UserProfilePage(container,user_info,self.frames)
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
         
         
class UserProfilePage(tk.Frame):
    
    def __init__(self, parent,user_info,frames):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        tk.Label(self,text="Username = ").grid(row=0,column=0)
        self.frames = frames
        tk.Label(self,text="Birth Date").grid(row=1)
        tk.Label(self,text="Email = ").grid(row=2)
        tk.Label(self,text="Country = ").grid(row=3)
        tk.Label(self,text="Zip Code = ").grid(row=4)
        tk.Label(self,text="Street = ").grid(row=5)
        ttk.Button(self,text="Login Page",command=lambda:self.login()).grid(row=6)
    def UpdateProfile(self,user_info):                 
        self.user_info = user_info
        print(user_info)
        tk.Label(self,text=user_info["user_name"]).grid(row=0,column=1)
        tk.Label(self,text=user_info["birth_date"]).grid(row=1,column=1)
        tk.Label(self,text=user_info["email"]).grid(row=2,column=1)
        tk.Label(self,text=user_info["country"]).grid(row=3,column=1)
        tk.Label(self,text=user_info["zip_code"]).grid(row=4,column=1)
        tk.Label(self,text=user_info["street"]).grid(row=5,column=1)
    def login(self):
        frame = self.frames[LoginPage]
        frame.tkraise()    
    
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

class SignUpPage(tk.Frame):
    
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

   


app = tkinterApp() 
app.mainloop() 


db.close()