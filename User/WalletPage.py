# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:09:38 2020

@author: Thanasis
"""
import tkinter as tk
from tkinter import ttk
from createToolbar import createToolbar


class WalletPage(tk.Frame):
    
     def __init__(self, parent, cur,user_info, frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.frames=frames
        self.user_info = user_info
        
        
        createToolbar(self, frames)
        tk.Label(self,text="How much money do you want to add?").grid(row=2,column=1)
        moneyToAdd=tk.Entry(self)
        moneyToAdd.grid(row=2,column=2)
        add_button=ttk.Button(self, text="Add", command=lambda: self.addMoney(str(moneyToAdd.get())))
        add_button.grid(row=3,column=2)
        
        
        
     def addMoney(self, money):
         try:
             instr="UPDATE wallet SET money=money+"+money+" WHERE user_id="+str(self.user_info["user_id"])
             self.cur.execute(instr)
             
             frame=self.frames["Wallet"]
             frame.show()
             frame.tkraise()
         except:
             tk.Label(self,text="Attention: NO MONEY ADDED").grid(row=3,column=1)
            
     def show_buyPlan(self):
        frame=self.frames["Store"]
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
        
     def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.tkraise()            