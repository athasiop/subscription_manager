# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:13:10 2020

@author: johni
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def createToolbar(self, frames):
    toolbarFrame = tk.Frame(self, bg = "lightgrey", borderwidth = 10)
    imgSize = 35, 35
    imgLogOut = Image.open("log-out.png")
    imgProfile = Image.open("profile.png")
    imgWallet = Image.open("wallet.png")
    imgStore = Image.open("store.png")
    imgTicket = Image.open("ticket.png")
    newImgLogOut = imgLogOut.resize(imgSize)
    newImgProfile = imgProfile.resize(imgSize)
    newImgWallet = imgWallet.resize(imgSize)
    newImgStore = imgStore.resize(imgSize)
    newImgTicket = imgTicket.resize(imgSize)
    toolbarFrame.photoLogout = ImageTk.PhotoImage(newImgLogOut) 
    toolbarFrame.photoProfile = ImageTk.PhotoImage(newImgProfile)
    toolbarFrame.photoWallet = ImageTk.PhotoImage(newImgWallet)
    toolbarFrame.photoStore = ImageTk.PhotoImage(newImgStore)
    toolbarFrame.photoTicket = ImageTk.PhotoImage(newImgTicket)
    ttk.Button(toolbarFrame,text = "Profile",image = toolbarFrame.photoProfile, compound = tk.RIGHT, command=self.profilePage).grid(row=0, column=0, padx = 50)
    ttk.Button(toolbarFrame,text = "Store", image = toolbarFrame.photoStore, compound = tk.RIGHT,command=self.show_buyPlan).grid(row=0, column=1, padx = 50)
    ttk.Button(toolbarFrame,text="Support Ticket",image = toolbarFrame.photoTicket, compound = tk.RIGHT,command=self.support_tickets).grid(row=0,column=2, padx = 50)
    ttk.Button(toolbarFrame,text = "Wallet",image = toolbarFrame.photoWallet, compound = tk.RIGHT,command=self.main_menu).grid(row=0,column=3, padx = 50)
    ttk.Button(toolbarFrame,text = "Log Out",image = toolbarFrame.photoLogout, compound = tk.RIGHT, command=self.logout).grid(row=0,column=4, padx = 50)
    toolbarFrame.grid(row = 0, column = 0, rowspan = 1, columnspan = 5)
    
    def main_menu(self):        
        frame = self.frames["Wallet"]
        frame.grid(row = 1, column = 0)
        frame.show()
        frame.tkraise()
    
    def support_tickets(self):
        frame = self.frames["SupportTicketList"]
        frame.grid(row = 1, column = 0)
        frame.RefreshList()
        frame.tkraise()
        
    def logout(self):
        frame = self.frames["LoginPage"]
        frame.grid(row = 1, column = 0)
        frame.tkraise()
        
    def show_buyPlan(self):
        frame=self.frames["Store"]
        frame.grid(row = 1, column = 0)
        frame.tkraise()
    
    def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.grid(row = 1, column = 0)
        frame.tkraise()