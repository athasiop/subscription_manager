import tkinter as tk
from tkinter import ttk
import datetime
from createToolbar import createToolbar
from tkinter import messagebox
from PIL import Image, ImageTk

class BuyPlan(tk.Frame): 
      
    def __init__(self,parent,cur,user_info,frames,loginWindow,mainWindow):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        self.loginWindow = loginWindow
        self.mainWindow = mainWindow
        
        imgSize = 25, 25
        imgSearch = Image.open(r"Images\search.png")
        newImgSearch= imgSearch.resize(imgSize)
        self.photoSearch = ImageTk.PhotoImage(newImgSearch)
        
        createToolbar(self, frames)
        show_all_button=tk.Button(self,text="Show all plans", command=lambda: self.showPlans(""))
        show_all_button.grid(row=1, column=2,sticky = tk.N, pady = 120)
        tk.Label(self, text="Search service name").grid(row=1,column=2,sticky = tk.N,pady = 30)
        search_bar=tk.Entry(self)
        search_bar.grid(row=1,column=2,sticky = tk.N, pady = 50)
        show_searched_button=tk.Button(self,text="Search", image = self.photoSearch, compound = tk.RIGHT,command=lambda: self.showPlans(search_bar.get()))
        show_searched_button.grid(row=1, column=2,sticky = tk.N, pady = 80)
        self.showPlans("")
        
    def showPlans(self,input):
        try:
            instr="SELECT * FROM subscription_plan WHERE service_name LIKE '%"+input+"%'"
            self.cur.execute(instr)
            self.tree=ttk.Treeview(self)
            self.tree.grid(row=1)
            verscrlbar = ttk.Scrollbar(self,  
                            orient ="vertical",  
                            command = self.tree.yview)
            verscrlbar.grid(row=1, column=1)
            self.tree.configure(xscrollcommand = verscrlbar.set)
            # Defining number of columns 
            self.tree["columns"] = ("1", "2", "3", "4", "5") 

            self.tree['show'] = 'headings'

            self.tree.column("1", width = 90, anchor ='c') 
            self.tree.column("2", width = 90, anchor ='c') 
            self.tree.column("3", width = 90, anchor ='c')
            self.tree.column("4", width = 90, anchor ='c') 
            self.tree.column("5", width = 90, anchor ='c') 

            self.tree.heading("1", text ="Service Name") 
            self.tree.heading("2", text ="Type") 
            self.tree.heading("3", text ="Price") 
            self.tree.heading("4", text ="Region") 
            self.tree.heading("5", text ="id") 

            while True:
                record = self.cur.fetchone()
                if record==None:
                    break
                self.tree.insert('', 'end',text="",values=(record[4],record[3],str(record[1])+"€", record[2], str(record[0])))
        except:
            print("k")    
        self.tree.bind("<Double-Button-1>", self.buy_plan) 
            
    def buy_plan(self,event):
         curReview = self.tree.focus()
         selectedRow = self.tree.item(curReview)
         service_name = str(selectedRow).split(", ")[2].split("'")[3]
         plan_id=str(selectedRow).split(", ")[6].split("]")[0]
         price=str(selectedRow).split(", ")[4].split("'")[1].replace("€","")
         MsgBox = messagebox.askquestion ('Attention','Are you sure you want to buy this plan?')
         if MsgBox=='yes':
              try:
                 instr="SELECT * FROM wallet WHERE user_id="+str(self.user_info["user_id"])
                 self.cur.execute(instr)
                 record=self.cur.fetchone()
                 currMoney=record[0]
                 newMoney=float(currMoney)-float(price)
                 if (newMoney<0):
                     messagebox.showinfo("Warning", "Not enough money")
                 else:
                     instr="INSERT INTO user_buys_subscription_plan (user_id, plan_id, service_name, plan_purchase_date) VALUES ("+str(self.user_info["user_id"])+"," +plan_id+ ", '" +service_name+ "','" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"')"
                     self.cur.execute(instr)
                     instr="UPDATE wallet SET money="+str(newMoney)+" WHERE user_id="+str(self.user_info["user_id"])
                     self.cur.execute(instr)
              except:
                  messagebox.showinfo("Warning", "You already own this plan")
        
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
        self.mainWindow.destroy()
        self.loginWindow.deiconify()
        
    def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.RefreshProfile()
        frame.tkraise()