import tkinter as tk

from Wallet import Wallet
from WalletPage import WalletPage
from BuyPlan import BuyPlan
from PaymentMethod import PaymentMethod
from UserProfilePage import UserProfilePage
from SupportTicketPage import SupportTicketPage
from SupportTicketList import SupportTicketList
from PaymentMethodPage import PaymentMethodPage
from Store import Store
from user_curPlans_reviews import CurrentPlans
from BuyBundle import BuyBundle





class MainMenu(tk.Toplevel):      

    def __init__(self,cur,user_info, loginWindow):  
         
        # __init__ function for class Tk 
        tk.Toplevel.__init__(self) 
        self.title("Subscription Manager")
        self.cur=cur
        self.user_info=user_info
        self.loginWindow = loginWindow
        self.protocol("WM_DELETE_WINDOW", lambda: self.loginWindow.destroy())
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
         
        self.frames = {}
        self.frames["UserProfilePage"] = UserProfilePage(container,cur,user_info,self.frames,self.loginWindow,self)        
        self.frames["SupportTicketPage"] = SupportTicketPage(container,cur,user_info,self.frames,self.loginWindow,self)        
        self.frames["SupportTicketList"] = SupportTicketList(container,cur,user_info,self.frames,self.loginWindow,self)       
        self.frames["Wallet"]=Wallet(container,cur,user_info,self.frames,self.loginWindow,self)                 
        self.frames["WalletPage"]=WalletPage(container,cur,user_info,self.frames,self.loginWindow,self)        
        self.frames["PaymentMethod"]=PaymentMethod(container, cur,user_info, self.frames,self.loginWindow,self)       
        self.frames["PaymentMethodPage"]=PaymentMethodPage(container, cur,user_info, self.frames)       
        self.frames["BuyPlan"]=BuyPlan(container,cur,user_info,self.frames,self.loginWindow,self)
        self.frames["CurrentPlans"] = CurrentPlans(container, cur, user_info ,self.frames,self.loginWindow,self)
        self.frames["Store"] = Store(container, cur, user_info ,self.frames,self.loginWindow,self)
        self.frames["BuyBundle"]=BuyBundle(container,cur,user_info,self.frames,self.loginWindow,self)
    
        
        self.frames["UserProfilePage"].grid(row=0,column=0,sticky="nsew")        
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
        
        
        
        self.show_frame("UserProfilePage")
        
        
        
        
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()