import tkinter as tk
from tkinter import ttk

class LoginPage(tk.Frame):
    
    def __init__(self,parent,cur,company_info,frames):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.company_info=company_info
        self.frames = frames
        
        tk.Label(self,text = "Enter Your Service Name").grid(row=0,column=0)
        entry_company_name = tk.Entry(self)
        entry_company_name.grid(row=0,column=1)
        
        
        
        login_button = ttk.Button(self,text="Log In",command=lambda:self.login(str(entry_company_name.get())))
        login_button.grid(row=1,column=0)
        
    def login(self,service_name):
        try:
            instr = "SELECT * FROM subscription_service WHERE service_name='"+service_name+"'"
            
            self.cur.execute(instr)
            record = self.cur.fetchone()
            self.company_info["service_name"]=record[0]
            
            #TODO add age
            
            frame = self.frames["CompanyPlans"]
           
            frame.show_info()
            frame.tkraise()
        except tk.TclError as e:
            print("Issue with tinker: "+str(e))
        except TypeError as e:
            self.service_not_found_label = tk.Label(self,text="User Not Found",bg="red")
            self.service_not_found_label.grid(row=3,column=0)
            self.after(3000, self.clear_label)
            print("Error: "+str(e))
    def clear_label(self):
        self.user_not_found_label.grid_forget()
        