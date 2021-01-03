import tkinter as tk

from Wallet import Wallet
from WalletPage import WalletPage
from BuyPlan import BuyPlan
from PaymentMethod import PaymentMethod
from SignUpPage import SignUpPage
from UserProfilePage import UserProfilePage
from LoginPage import LoginPage
from SupportTicketPage import SupportTicketPage
from SupportTicketList import SupportTicketList
from PaymentMethodPage import PaymentMethodPage
from Store import Store
from user_curPlans_reviews import CurrentPlans
from BuyBundle import BuyBundle

class tkinterApp(tk.Tk):      
    # __init__ function for class tkinterApp  
    def __init__(self,cur,user_info):  
         
        # __init__ function for class Tk 
        tk.Tk.__init__(self) 
        self.title("Subscription Manager")
        self.cur=cur
        self.user_info=user_info
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
         
        self.frames = {}
        self.frames["SignUpPage"] = SignUpPage(container,cur,user_info,self.frames)      
        self.frames["UserProfilePage"] = UserProfilePage(container,cur,user_info,self.frames)        
        self.frames["LoginPage"] = LoginPage(container,cur,user_info,self.frames)        
        self.frames["SupportTicketPage"] = SupportTicketPage(container,cur,user_info,self.frames)        
        self.frames["SupportTicketList"] = SupportTicketList(container,cur,user_info,self.frames)       
        self.frames["Wallet"]=Wallet(container,cur,user_info,self.frames)                 
        self.frames["WalletPage"]=WalletPage(container,cur,user_info,self.frames)        
        self.frames["PaymentMethod"]=PaymentMethod(container, cur,user_info, self.frames)       
        self.frames["PaymentMethodPage"]=PaymentMethodPage(container, cur,user_info, self.frames)       
        self.frames["BuyPlan"]=BuyPlan(container,cur,user_info,self.frames)
        self.frames["CurrentPlans"] = CurrentPlans(container, cur, user_info ,self.frames)
        self.frames["Store"] = Store(container, cur, user_info ,self.frames)
        self.frames["BuyBundle"]=BuyBundle(container,cur,user_info,self.frames)
    
        
        self.frames["SignUpPage"].grid(row=0,column=0,sticky="nsew")   
        self.frames["UserProfilePage"].grid(row=0,column=0,sticky="nsew")        
        self.frames["LoginPage"].grid(row=0,column=0,sticky="nsew")       
        self.frames["SupportTicketPage"].grid(row=0,column=0,sticky="nsew")     
        self.frames["SupportTicketList"].grid(row=0,column=0,sticky="nsew")               
        self.frames["Wallet"].grid(row=0, column=0, sticky="nsew")     
        self.frames["WalletPage"].grid(row=0, column=0, sticky="nsew")       
        self.frames["PaymentMethodPage"].grid(row=0, column=0, sticky="nsew")      
        self.frames["PaymentMethod"].grid(row=0, column=0, sticky="nsew")       
        self.frames["BuyPlan"].grid(row=0, column=0, sticky="nsew")
        self.frames["CurrentPlans"].grid(row=0,column=0,sticky="nsew")
        self.frames["Store"].grid(row=0,column=0,sticky="nsew")
        self.frames["BuyBundle"].grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginPage") 
        
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()