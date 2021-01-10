import tkinter as tk
from tkinter import ttk
from tkinter import Text
from createToolbar import createToolbar

class SupportTicketPage(tk.Frame):
    def __init__(self,parent,cur,user_info,frames,loginWindow,mainWindow):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        self.loginWindow = loginWindow
        self.mainWindow = mainWindow
        
        createToolbar(self, frames)
        tk.Label(self,text="Insert Your Question").grid(row=1,column=0)
        self.questionEntry = Text(self,height=10,width=40)
        self.questionEntry.grid(row=2)
        send_button = ttk.Button(self,text="Submit",command = self.send_ticket)
        send_button.grid(row=3)
        
    def send_ticket(self):
        question = self.questionEntry.get("1.0",tk.END)
        instr = "INSERT INTO support_ticket (user_id,question)VALUES('"+str(self.user_info["user_id"])+"','"+str(question)+"')"
        self.questionEntry.delete('1.0',tk.END)
        try:
            self.cur.execute(instr)
        except:
            print("Unable to send support ticket")
        frame = self.frames["SupportTicketList"]
        frame.RefreshList()
        frame.tkraise()
        
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