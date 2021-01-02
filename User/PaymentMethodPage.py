# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:08:36 2020

@author: Thanasis
"""
import tkinter as tk

class PaymentMethodPage(tk.Frame):    
    
    def __init__(self, parent, cur,user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info = user_info

        paymentMethods=['Credit Card', 'Debit Card', 'Paypal', 'Paysafe']
       
        
        self.vars = []
        for i in range(0,len(paymentMethods)):
            var=tk.IntVar()
            tk.Checkbutton(self, text=paymentMethods[i], variable=var).grid(row=i)
            self.vars.append(var)
            
        tk.Button(self, text="Add Payment Method", command=lambda: self.addPayment()).grid(row=len(paymentMethods)+1)
        
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
            tk.messagebox.showinfo("Warning", "You already have this payment method")
        frame=self.frames["PaymentMethod"]
        frame.show() 
        frame.tkraise() 