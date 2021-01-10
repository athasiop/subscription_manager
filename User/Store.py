import tkinter as tk
from createToolbar import createToolbar

class Store(tk.Frame):    
    def __init__(self,parent,cur,user_info,frames,loginWindow,mainWindow):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        self.loginWindow = loginWindow
        self.mainWindow = mainWindow
        
        createToolbar(self, frames)
        # label=tk.Label(self, text="MAIN MENU")
        # label.grid(row=0, column=1,pady=10, padx=10)
        add_money_button=tk.Button(self, text="Buy a Plan", command=lambda: self.buyPlan())
        add_money_button.grid(row=1, column=1,pady=10, padx=10)
        payment_method_button=tk.Button(self, text="Buy a Bundle", command=lambda: self.buyBundle())
        payment_method_button.grid(row=2, column=1,pady=10, padx=10)
        # buy_plan_button=tk.Button(self, text="Buy Plans", command=lambda: self.show_buyPlan())
        # buy_plan_button.grid(row=3,column=1,pady=10,padx=10)
        
        

    def buyPlan(self):
        frame=self.frames["BuyPlan"]
        frame.tkraise()
        
    def buyBundle(self):
        frame=self.frames["BuyBundle"]
        frame.tkraise()
#TOOLBAR        
    def main_menu(self):        
        frame = self.frames["Wallet"]
        frame.show()
        frame.tkraise()
    
    def support_tickets(self):
        frame = self.frames["SupportTicketList"]
        frame.RefreshList()
        frame.tkraise()
        
    def logout(self):
        self.mainWindow.destroy()
        self.loginWindow.deiconify()
        
    def show_buyPlan(self):
        frame=self.frames["Store"]
        frame.tkraise()
    
    def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.RefreshProfile()
        frame.tkraise()