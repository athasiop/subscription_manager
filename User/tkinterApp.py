import tkinter as tk


from SignUpPage import SignUpPage
from LoginPage import LoginPage


class tkinterApp(tk.Tk):      
    # __init__ function for class tkinterApp  
    def __init__(self,cur,user_info):  
         
        # __init__ function for class Tk 
        tk.Tk.__init__(self) 
        self.title("Subscription Manager")
        self.cur=cur
        self.user_info=user_info
        self.geometry("420x420")
        self.resizable(False, False)
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
         
        self.frames = {}
        self.frames["SignUpPage"] = SignUpPage(container,cur,user_info,self.frames, self)      
        self.frames["LoginPage"] = LoginPage(container,cur,user_info,self.frames, self)        
       
    
        
        self.frames["SignUpPage"].grid(row=0,column=0,sticky="nsew")          
        self.frames["LoginPage"].grid(row=0,column=0,sticky="nsew")       
        
        
        self.show_frame("LoginPage") 
        
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()