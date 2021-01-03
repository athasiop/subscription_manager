import tkinter as tk
from createToolbar import createToolbar

class PaymentMethod(tk.Frame):
    
    def __init__(self, parent, cur,user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info = user_info

        show_button=tk.Button(self, text="Show Payment Methods", command=lambda: self.show())
        show_button.grid(row=1)
        add_payment_button=tk.Button(self, text="Add Payment Method", command=lambda: self.addPayment())
        add_payment_button.grid(row=2)
        createToolbar(self,frames)
        
    def show(self):
        try:
            instr="SELECT payment_method FROM payment_method WHERE user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            i=1;
            while True:
                record = self.cur.fetchone()
                if record==None:
                    break
                tk.Label(self,text=str(record[0])).grid(row=i+2)
                i=i+1

        except:
            print("User Not Found!")
        
    def addPayment(self):
        frame=self.frames["PaymentMethodPage"]
        frame.tkraise()
        
    def main_menu(self):        
        frame = self.frames["Wallet"]
        frame.show()
        frame.tkraise()
    
    def support_tickets(self):
        frame = self.frames["SupportTicketList"]
        frame.RefreshList()
        frame.tkraise()
        
    def logout(self):
        frame = self.frames["LoginPage"]
        frame.tkraise()
        
    def show_buyPlan(self):
        frame=self.frames["Store"]
        frame.tkraise()
    
    def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.tkraise()