# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:09:11 2020

@author: Thanasis
"""
import tkinter as tk
from tkinter import ttk
from createToolbar import createToolbar

class SupportTicketList(tk.Frame):
     
     def __init__(self,parent,cur,user_info,frames):
        tk.Frame.__init__(self, parent)
        self.user_info = user_info
        self.frames = frames
        self.cur = cur
        
        self.labels = []
        tk.Label(self,text="Questions").grid(row=1,column=0)
        tk.Label(self,text="Answers").grid(row=1,column=1)
        self.new_support_ticket_button = ttk.Button(self,text="Send New Support Ticket",command = self.send_support_ticket)
        self.return_to_profile_button = ttk.Button(self,text="Return To Profile",command = self.return_to_profile)
        createToolbar(self, frames)

     def RefreshList(self):
        
        self.labels.clear()
        k = self.select_support_ticket("question",0)
        self.select_support_ticket("answer",1)
                
        self.new_support_ticket_button.grid(row=k)
        self.return_to_profile_button.grid(row=k,column=1)
        
     def select_support_ticket(self,returnval,col):
              
        instr = "SELECT "+returnval+" FROM support_ticket WHERE user_id='"+str(self.user_info["user_id"])+"'"
        self.cur.execute(instr)
        k=2
        for i in self.cur.fetchall():            
            q = str(i)            
            q = q.replace("'","")
            q = q.replace("(", "")
            q = q.replace(")", "")
            q = q.replace("\\n", "")
            q = q.replace(",", "")
                        
            self.labels.append(tk.Label(self,text=q))
            self.labels[-1].grid(row=k,column=col)
            k=k+1
        return k
    
     def send_support_ticket(self):
         frame = self.frames["SupportTicketPage"]
         for i in self.labels:
          i.destroy()
         
         frame.tkraise()
         
     def return_to_profile(self):
         frame = self.frames["UserProfilePage"]
         for i in self.labels:
          i.destroy()
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