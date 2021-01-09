import tkinter as tk


from CompanyLoginPage import LoginPage
from ReviewsPage import ReviewsPage
from CompanyPlans import CompanyPlans

class tkinterApp(tk.Tk):      
    # __init__ function for class tkinterApp  
    def __init__(self,cur,company_info):  
         
        # __init__ function for class Tk 
        tk.Tk.__init__(self) 
        self.cur=cur
        self.company_info=company_info
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
         
        self.frames = {}
              
          
        self.frames["LoginPage"] = LoginPage(container,cur,company_info,self.frames)        
        self.frames["ReviewsPage"] = ReviewsPage(container,cur,company_info,self.frames)
        self.frames["CompanyPlans"] = CompanyPlans(container,cur,company_info,self.frames)
         
      
        
        self.frames["ReviewsPage"].grid(row=0,column=0,sticky="nsew") 
        self.frames["CompanyPlans"].grid(row=0,column=0,sticky="nsew")
        self.frames["LoginPage"].grid(row=0,column=0,sticky="nsew")       
        
        
        self.show_frame("LoginPage") 
        
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()