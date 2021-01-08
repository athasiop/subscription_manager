import tkinter as tk
from tkinter import ttk
from createToolbar import createToolbar
from PIL import Image, ImageTk

class SupportTicketList(tk.Frame):
     
     def __init__(self,parent,cur,user_info,frames,loginWindow,mainWindow):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        self.loginWindow = loginWindow
        self.mainWindow = mainWindow
        
        imgSize = 30, 30
        imgNewTicket = Image.open(r"Images\newTicket.png")
        newImgNewTicket = imgNewTicket.resize(imgSize) 
        self.photoAddImgNewTicket = ImageTk.PhotoImage(newImgNewTicket)
        
        tk.Label(self, text = "Last 4 support tickets", font = 'Helvetica 10 italic').place(x = 380, y = 83)
        self.labels = []
        tk.Label(self,text="Questions",font='Helvetica 12 bold').grid(row=1,column=0)
        tk.Label(self,text="Answers",font='Helvetica 12 bold').grid(row=1,column=1, pady = 5)
        self.new_support_ticket_button = ttk.Button(self,text="New Ticket", image = self.photoAddImgNewTicket, compound = tk.RIGHT, command = self.send_support_ticket)
        self.new_support_ticket_button.grid(row=1, column = 2, pady = 10)
        createToolbar(self, frames)

     def RefreshList(self):
        
        self.labels.clear()
        self.select_support_ticket("question",0)
        self.select_support_ticket("answer",1)
        
                
        
        
     def select_support_ticket(self,returnval,col):
              
        instr = "SELECT "+returnval+" FROM support_ticket WHERE user_id='"+str(self.user_info["user_id"])+"'"
        self.cur.execute(instr)
        temp=self.cur.fetchall()
        k=4
        for i in temp[len(temp)-4:len(temp)]:
            q = str(i)            
            q = q.replace("'","")
            q = q.replace("(", "")
            q = q.replace(")", "")
            q = q.replace("\\n", "")
            q = q.replace(",", "")
            
            textT = tk.Text(self, height = 3, width = 50)
            textT.insert(tk.END, q)  
            textT.config(state=tk.DISABLED)
            self.labels.insert(0, textT)
            self.labels[0].grid(row = k + 2, column = col)
            k = k - 1
           
        
        
        return k
    
    
    
     def send_support_ticket(self):
         frame = self.frames["SupportTicketPage"]
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
        self.mainWindow.destroy()
        self.loginWindow.deiconify()
        
     def show_buyPlan(self):
        frame=self.frames["Store"]
        frame.tkraise()
    
     def profilePage(self):
        frame=self.frames["UserProfilePage"]
        frame.tkraise()