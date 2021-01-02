# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:24:43 2020

@author: Thanasis
"""
import tkinter as tk
from tkinter import ttk
import datetime

class ReviewsPage(tk.Frame):
     
     def __init__(self,parent,cur,company_info,frames):
        tk.Frame.__init__(self, parent)
        self.company_info = company_info
        self.frames = frames
        self.cur = cur
        self.avg_rating=0
        self.labels = []
        tk.Label(self,text="Comment",font=(20)).grid(row=0,column=0)
        tk.Label(self,text="Rating",font=(20)).grid(row=0,column=1)
        tk.Label(self,text="Time Of Review",font=(20)).grid(row=0,column=2)
        tk.Label(self,text="Average Rating",font=(20)).grid(row=0,column=3)
        
    
     def show_plans(self):
         frame = self.frames["CompanyPlans"]
         for i in self.labels:
                i.destroy()
         frame.show_info()
         frame.tkraise()
         
     def RefreshList(self):
        self.avg_rating=0                
        self.select_review_col("comment",0)
        k=self.select_review_col("rating",1)
        self.select_review_time(2)     
        ttk.Button(self,text="Show Plans",command=self.show_plans).grid(row=k)
        
     def select_review_col(self,returnval,col):
              
        instr = "SELECT "+ returnval+" FROM user_reviews_service WHERE service_name='"+str(self.company_info["service_name"])+"'"
        self.cur.execute(instr)
        k=1
        
        for i in self.cur.fetchall():            
            q = str(i)            
            q = q.replace("'","")
            q = q.replace("(", "")
            q = q.replace(")", "")
            q = q.replace("\\n", "")
            q = q.replace(",", "")
                        
            self.labels.append(tk.Label(self,text=q))
            if returnval=="rating":
                self.avg_rating=(self.avg_rating+int(q))/k
            self.labels[-1].grid(row=k,column=col)
            k=k+1
        if returnval=="rating":
            tk.Label(self,text=str(round(self.avg_rating,2)),font=("Calibri", 30)).grid(row=int(k/2),column=3)
        return k
     def select_review_time(self,col):
            
            instr = "SELECT review_date FROM user_reviews_service WHERE service_name='"+str(self.company_info["service_name"])+"'"
            self.cur.execute(instr)
            k=1
            for i in self.cur.fetchall():
                q = str(i).replace("(", "").replace(")", "").replace(" ","").replace("datetime.datetime", "").replace("\\n", "")           
                q = q.split(",")
                        
                self.labels.append(tk.Label(self,text=q[0]+"-"+ q[1]+"-"+ q[2]))
                
                self.labels[-1].grid(row=k,column=col)
                k=k+1
            return k 
     