# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:30:28 2020

@author: johni
"""
import pymysql as sql
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
import time

user_info = {
    "user_id":"",
    "money":""
}

db = sql.connect("127.0.0.1","user","pass","subscription_manager",autocommit=True)
cur = db.cursor()


class Container(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        container=tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames={} 
        self.frames[MainMenu]=MainMenu(container,cur,user_info,self.frames)     
        self.frames[MainMenu].grid(row=0, column=0, sticky="nsew")     
        self.frames[Wallet]=Wallet(container,cur,user_info,self.frames)
        self.frames[Wallet].grid(row=0, column=0, sticky="nsew")  
        self.frames[WalletPage]=WalletPage(container,cur, user_info,self.frames)
        self.frames[WalletPage].grid(row=0, column=0, sticky="nsew")
        self.frames[PaymentMethod]=PaymentMethod(container, cur, user_info, self.frames)
        self.frames[PaymentMethod].grid(row=0, column=0, sticky="nsew")
        self.frames[PaymentMethodPage]=PaymentMethodPage(container, cur, user_info, self.frames)
        self.frames[PaymentMethodPage].grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainMenu)
        
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
            
class MainMenu(tk.Frame):
    
    def __init__(self,parent,cur, user_info,frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.frames=frames
        self.user_info=user_info
        
        label=tk.Label(self, text="MAIN MENU")
        label.pack(pady=10, padx=10)
        wallet_button=ttk.Button(self, text="Wallet",
                                command=lambda: self.show_Wallet())
        wallet_button.pack()
        payment_method_button=ttk.Button(self, text="Payment Methods", command=lambda: self.show_PM())
        payment_method_button.pack()
        
    def show_Wallet(self):
        frame = self.frames[Wallet]
        frame.tkraise()
        
    def show_PM(self):
        frame=self.frames[PaymentMethod]
        frame.tkraise()
        
class Wallet(tk.Frame):
    
    def __init__(self, parent, cur, user_info,frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.frames=frames
        self.user_info=user_info
        
        show_button=tk.Button(self, text="Show Wallet", command=lambda: self.show())
        show_button.grid(row=1)
        add_money_button=tk.Button(self, text="Add Money", command=lambda: self.addMoney())
        add_money_button.grid(row=2)
    
    def show(self):
        try:
            instr="SELECT * FROM wallet WHERE user_id=6"
            self.cur.execute(instr)
            
            record = self.cur.fetchone()
        except:
            print("User Not Found!")
        
        tk.Label(self,text="You have " + str(record[0]) + "€ in your account").grid(row=3)
    
    def addMoney(self):
        frame=self.frames[WalletPage]
        frame.tkraise()
      
            
class WalletPage(tk.Frame):
    
     def __init__(self, parent, cur, user_info, frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.frames=frames
        self.user_info=user_info
        
        tk.Label(self,text="How much money do you want to add?").grid(row=1,column=1)
        moneyToAdd=tk.Entry(self)
        moneyToAdd.grid(row=1,column=2)
        add_button=ttk.Button(self, text="Add", command=lambda: self.addMoney(str(moneyToAdd.get())))
        add_button.grid(row=2,column=2)
        
        
     def addMoney(self, money):
         try:
             instr="UPDATE wallet SET money=money+"+money+" WHERE user_id=6"
             self.cur.execute(instr)
             time.sleep(1)
             frame=self.frames[Wallet]
             frame.show()
             frame.tkraise()
         except:
            tk.Label(self,text="Attention: NO MONEY ADDED").grid(row=3,column=1)
            
        
     def UpdateProfile(self):
        tk.Label(self,text=self.user_info["user_id"]).grid(row=1,column=1)
        tk.Label(self,text=self.user_info["money"]).grid(row=2,column=1)
            
class PaymentMethod(tk.Frame):
    
    def __init__(self, parent, cur, user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info=user_info
        
        show_button=tk.Button(self, text="Show Payment Methods", command=lambda: self.show())
        show_button.grid(row=1)
        add_payment_button=tk.Button(self, text="Add Payment Method", command=lambda: self.addPayment())
        add_payment_button.grid(row=2)
        
    def show(self):
        try:
            instr="SELECT payment_method FROM payment_method WHERE user_id=4"
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
        frame=self.frames[PaymentMethodPage]
        frame.tkraise()   
 
        
class PaymentMethodPage(tk.Frame):    
    
    def __init__(self, parent, cur, user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info=user_info
        
        paymentMethods=['Credit Card', 'Debit Card', 'Paypal', 'Paysafe']
       
        
        self.vars = []
        for i in range(0,len(paymentMethods)):
            var=IntVar()
            tk.Checkbutton(self, text=paymentMethods[i], variable=var).grid(row=i)
            self.vars.append(var)
            
        tk.Button(self, text="Add Payment Method", command=lambda: self.addPayment()).grid(row=len(paymentMethods)+1)
        
    def state(self):
      return map((lambda var: var.get()), self.vars)
            
    def addPayment(self):
        print((list(self.state())))
        try:
            k=0
            for i in list(self.state()):
                if i==0:
                    k=k+1
                    continue
                else:
                    instr="INSERT INTO payment_method (payment_method, user_id) VALUES ("+str(k+1)+", 4)"
                    self.cur.execute(instr)
                k=k+1  
        except:
            print("NOT ADDED. Check if you already have it")
        frame=self.frames[PaymentMethod]
        frame.show() 
        frame.tkraise() 
            
        
              
    
        
app=Container()
app.mainloop()

db.close()
        
        
        
        