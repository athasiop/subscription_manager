import tkinter as tk
from tkinter import ttk

class ReviewsPage(tk.Frame):
     
     def __init__(self,parent,cur,company_info,frames):
        tk.Frame.__init__(self, parent)
        self.company_info = company_info
        self.frames = frames
        self.cur = cur
        self.avg_rating=0
        self.labels = []
        tk.Label(self,text="Comment",font=(20)).grid(row=0,column=0,padx=5)
        tk.Label(self,text="Rating",font=(20)).grid(row=0,column=1,padx=5)
        tk.Label(self,text="Review Date",font=(20)).grid(row=0,column=2,padx=5)
        tk.Label(self,text="Average Rating",font=(20)).grid(row=0,column=3,padx=5)
        
    
     def show_plans(self):
         frame = self.frames["CompanyPlans"]
         for i in self.labels:
                i.destroy()
         frame.show_info()
         frame.tkraise()
         
     def RefreshList(self):
        self.avg_rating=0                
        self.select_review_col("comment",0)
        self.select_review_col("rating",1)
        self.select_review_time(2)     
        ttk.Button(self,text="Show Plans",command=self.show_plans).grid(row=2,column=3)
        
     def select_review_col(self,returnval,col):
              
        instr = "SELECT "+ returnval+" FROM user_reviews_service WHERE service_name='"+str(self.company_info["service_name"])+"'"
        self.cur.execute(instr)
        temp=self.cur.fetchall()
        
        k=1
        for i in temp:
            q = str(i)            
            q = q.replace("'","")
            q = q.replace("(", "")
            q = q.replace(")", "")
            q = q.replace("\\n", "")
            q = q.replace(",", "")
            
            
            if returnval=="rating":
                labelT = tk.Label(self,text=q)
                self.labels.append(labelT)
                self.labels[-1].grid(row = k, column = col,padx=5) 
                self.avg_rating=(self.avg_rating+int(q))/k
            else:
                textT = tk.Text(self, height = 2, width = 30)
                textT.insert(tk.END, q)  
                textT.config(state=tk.DISABLED)
                self.labels.append(textT)
                self.labels[-1].grid(row = k, column = col,padx=5) 
            k=k+1
        if returnval=="rating":
            tk.Label(self,text=str(round(self.avg_rating,2)),font=("Calibri", 30)).grid(row=1,column=3)
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
     