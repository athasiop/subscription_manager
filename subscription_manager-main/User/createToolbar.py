# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:13:10 2020

@author: johni
"""
import tkinter as tk
from tkinter import ttk

def createToolbar(self, frames):
    ttk.Button(self,text="Profile",command=self.profilePage).grid(row=0, column=0)
    ttk.Button(self,text="Store",command=self.show_buyPlan).grid(row=0, column=1)
    ttk.Button(self,text="Support Ticket",command=self.support_tickets).grid(row=0,column=2)
    ttk.Button(self,text="Wallet",command=self.main_menu).grid(row=0,column=3)
    ttk.Button(self,text="Log Out",command=self.logout).grid(row=0,column=4)
    
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