import tkinter as tk
from tkinter import ttk
from tkinter import Text

class SupportTicketPage(tk.Frame):
    def __init__(self,parent,cur,user_info,frames):
        tk.Frame.__init__(self, parent)
        self.user_info = user_info
        self.frames = frames
        self.cur = cur
        
        tk.Label(self,text="Insert Your Question").grid(row=0,column=0)
        self.questionEntry = Text(self,height=10,width=40)
        self.questionEntry.grid(row=1)
        send_button = ttk.Button(self,text="send",command = self.send_ticket)
        send_button.grid(row=2)
        
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
        
        