# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:50:51 2021

@author: johni
"""

import tkinter as tk
from tkinter import ttk
import datetime
from createToolbar import createToolbar

class BuyBundle(tk.Frame): 
      
    def __init__(self, parent, cur,user_info, frames):
        tk.Frame.__init__(self,parent)
        self.cur=cur
        self.frames=frames
        self.user_info = user_info
        
        createToolbar(self, frames)
        show_all_button=tk.Button(self,text="Show bundles", command=lambda: self.showPlans(""))
        show_all_button.grid(row=1, column=0)

        
    def showPlans(self,input):
        try:
            instr="SELECT * FROM bundle JOIN bundle_price ON bundle_price.bundle_id=bundle.bundle_id"
            self.cur.execute(instr)
            self.tree=ttk.Treeview(self)
            self.tree.grid(row=4)
            verscrlbar = ttk.Scrollbar(self,  
                            orient ="vertical",  
                            command = self.tree.yview)
            verscrlbar.grid(row=4, column=1)
            self.tree.configure(xscrollcommand = verscrlbar.set)
            # Defining number of columns 
            self.tree["columns"] = ("1", "2", "3", "4") 

            # self.tree['show'] = 'headings'

            self.tree.column("1", width = 90, anchor ='c') 
            self.tree.column("2", width = 90, anchor ='c') 
            self.tree.column("3", width = 90, anchor ='c')
            self.tree.column("4", width = 90, anchor ='c') 
            
            self.tree.heading("1", text ="Discount") 
            self.tree.heading("2", text ="Service Name") 
            self.tree.heading("3", text ="Type") 
            self.tree.heading("4", text ="Price") 
            

            while True:
                record = self.cur.fetchone()
                if record==None:
                    break
                self.tree.insert("", 'end', "id"+str(record[0]),text=str(record[0]),values=(record[1],"", "", record[3]))                
        except:
            print("SQL Problem")
         

        try:
            instr="SELECT bundle.bundle_id,subscription_plan.service_name, plan_type, discount, total_bundle_price FROM ((bundle " +\
                  "JOIN bundle_contains_subscription_plan ON bundle.bundle_id = bundle_contains_subscription_plan.bundle_id) " +\
                  "JOIN subscription_plan ON bundle_contains_subscription_plan.plan_id=subscription_plan.plan_id " +\
                  "AND bundle_contains_subscription_plan.service_name=subscription_plan.service_name) " +\
                  "JOIN bundle_price ON bundle_price.bundle_id=bundle.bundle_id"
            self.cur.execute(instr)
            while True:
                record = self.cur.fetchone()
                if record==None:
                    break
                self.tree.insert("id"+str(record[0]), 'end',text="",values=("", record[1], record[2], ""))
        except:
            print("0")
            
        self.tree.bind("<Double-Button-1>", self.buy_plan)
                  
    def buy_plan(self,event):
         curReview = self.tree.focus()
         selectedRow = self.tree.item(curReview)
         bundle_id=str(selectedRow).split(", ")[0].split("'")[3]
         MsgBox = tk.messagebox.askquestion ('Attention','Are you sure you want to buy this bundle?')
         if MsgBox=='yes':
              try:
                 instr="INSERT INTO user_buys_bundle (user_id, bundle_id, bundle_purchase_date) VALUES ("+str(self.user_info["user_id"])+"," +bundle_id+ ",'" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"')"
                 self.cur.execute(instr)
              except:
                  tk.messagebox.showinfo("Warning", "You already own this bundle")
        
    #TOOLBAR        
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