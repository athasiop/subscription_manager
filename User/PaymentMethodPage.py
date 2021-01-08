import tkinter as tk
from tkinter import messagebox
from createToolbar import createToolbar

class PaymentMethodPage(tk.Frame):    
    
    def __init__(self, parent, cur,user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info = user_info

        paymentMethods=['Credit Card', 'Debit Card', 'Paypal', 'Paysafe']
       
        createToolbar(self, frames)
        self.vars = []
        for i in range(0,len(paymentMethods)):
            var=tk.IntVar()
            tk.Checkbutton(self, text=paymentMethods[i], variable=var).grid(row=i+1)
            self.vars.append(var)
            
        tk.Button(self, text="Add Payment Method", command=lambda: self.addPayment()).grid(row=len(paymentMethods)+2)
        
    def state(self):
      return map((lambda var: var.get()), self.vars)
            
    def addPayment(self):
        
        try:
            k=0
            for i in list(self.state()):
                if i==0:
                    k=k+1
                    continue
                else:
                    instr="INSERT INTO payment_method (payment_method, user_id) VALUES ("+str(k+1)+","+str(self.user_info["user_id"])+")"
                    self.cur.execute(instr)
                k=k+1  
        except:
            messagebox.showinfo("Warning", "You already have this payment method")
        frame=self.frames["PaymentMethod"]
        frame.show() 
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
        self.mainWindow.destroy()
        self.loginWindow.deiconify()
        
    def show_buyPlan(self):
        frame=self.frames["Store"]
        frame.tkraise()
    
    def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.tkraise()