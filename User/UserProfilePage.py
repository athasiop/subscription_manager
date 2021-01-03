import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, RIGHT
from tkinter import messagebox
from createToolbar import createToolbar
from PIL import Image, ImageTk

class UserProfilePage(tk.Frame):
    
    def __init__(self,parent,cur,user_info,frames):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        
        
        createToolbar(self, frames)
        
        imgSize = 20, 20
        imgEdit = Image.open("edit.png")
        imgDelete = Image.open("delete.png")
        imgUpdate = Image.open("update.png")
        newImgEdit = imgEdit.resize(imgSize)
        newImgDelete = imgDelete.resize(imgSize)
        newImgUpdate = imgUpdate.resize(imgSize)
        self.photoEdit = ImageTk.PhotoImage(newImgEdit) 
        self.photoDelete = ImageTk.PhotoImage(newImgDelete)
        self.photoUpdate = ImageTk.PhotoImage(newImgUpdate)
        
         
        #TODO Edit image
        tk.Label(self,text="Username = ").grid(row=1, column = 0, pady = 30)
        tk.Button(self, image = self.photoEdit, command=self.editName).grid(row=1, column=2, sticky = tk.W)
        
        tk.Label(self,text="Birth Date").grid(row=2, column = 0)
        tk.Label(self,text="Email = ").grid(row=3, column = 0)
        tk.Button(self, image = self.photoEdit, command=self.editEmail).grid(row=3, column=2, sticky = tk.W)
        tk.Label(self,text="Country = ").grid(row=4, column = 0)
        tk.Button(self, image = self.photoEdit, command=self.editCountry).grid(row=4, column=2, sticky = tk.W)
        tk.Label(self,text="Zip Code = ").grid(row=5, column = 0)
        tk.Button(self, image = self.photoEdit, command=self.editZipCode).grid(row=5, column=2, sticky = tk.W)
        tk.Label(self,text="Street = ").grid(row=6, column = 0)
        tk.Button(self, image = self.photoEdit, command=self.editStreet).grid(row=6, column=2, sticky = tk.W)
        ttk.Button(self,text="Delete Account",image = self.photoDelete, compound = tk.RIGHT,command=self.delete_user).grid(row=8,column=1, sticky = tk.W)
        ttk.Button(self,text="Show Current Plans",command=self.show_current_plans).grid(row=8,column=0)
        self.update_button = ttk.Button(self,text="Update Info",image = self.photoUpdate, compound = tk.RIGHT, command=self.update_info)
        self.update_button.configure(state="disabled")
        self.update_button.grid(row=8,column=2, pady = 20, sticky = tk.W)
        
#Show money        
    def show(self):
        try:
            instr="SELECT * FROM wallet WHERE user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            record = self.cur.fetchone()
        except:
            print("User Not Found!")
        
        tk.Label(self,text="You have " + str(record[0]) + "€ in your account").grid(row=1, column=3)   
#Unblock entries to edit        
    def editName(self):
        self.e1.config(state='normal')
        
    def editEmail(self):
        self.e3.config(state='normal')
    
    def editCountry(self):
        self.e4.config(state='normal')
    
    def editZipCode(self):
        self.e5.config(state='normal')
    
    def editStreet(self):
        self.e6.config(state='normal')

    def show_current_plans(self):
        frame = self.frames["CurrentPlans"]
        frame.show()
        frame.tkraise()
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
        
#Update info        
    def update_info(self):        
        self.user_info["user_name"] = str(self.e1.get())
        self.user_info["birth_date"] = str(self.e2.get())
        self.user_info["email"] = str(self.e3.get())
        self.user_info["country"] = str(self.e4.get())
        self.user_info["zip_code"] = str(self.e5.get())
        self.user_info["street"] = str(self.e6.get())       
        instr = "UPDATE user SET user_name='"+self.user_info["user_name"]+"',email='"+self.user_info["email"]+"',country='"+self.user_info["country"]+"',birth_date='"+self.user_info["birth_date"]+"',zip_code='"+ self.user_info["zip_code"]+"',street='"+self.user_info["street"]+"' WHERE user_id="+str(self.user_info["user_id"])

        try:
            self.cur.execute(instr)
            
            self.update_success = tk.Label(self,text="Update Successfull",bg="green")
            self.update_success.grid(row=7,column=2)
            self.after(3000, self.clear_label)
        except:         
            print("SQL issue")
        self.e1.config(state='disabled')
        self.e3.config(state='disabled')
        self.e4.config(state='disabled')
        self.e5.config(state='disabled')
        self.e6.config(state='disabled')
            
    def clear_label(self):
        self.update_success.grid_forget()
        
    def UpdateProfile(self):
        
        sv1 = tk.StringVar()
        sv1.set(self.user_info["user_name"])
        sv1.trace("w", lambda name, index, mode, sv=sv1: self.callback())
        self.e1 = tk.Entry(self, textvariable=sv1, state='disabled')
        self.e1.grid(row=1,column=1, sticky = tk.W)
        
        sv2 = tk.StringVar()
        sv2.set(self.user_info["birth_date"])
        sv2.trace("w", lambda name, index, mode, sv=sv2: self.callback())
        self.e2 = tk.Entry(self, textvariable=sv2, state='disabled')
        self.e2.grid(row=2,column=1, sticky = tk.W)
                
        sv3 = tk.StringVar()
        sv3.set(self.user_info["email"])
        sv3.trace("w", lambda name, index, mode, sv=sv3: self.callback())
        self.e3 = tk.Entry(self, textvariable=sv3, state='disabled')
        self.e3.grid(row=3,column=1, sticky = tk.W)
        
        sv4 = tk.StringVar()
        sv4.set(self.user_info["country"])
        sv4.trace("w", lambda name, index, mode, sv=sv4: self.callback())
        self.e4 = tk.Entry(self, textvariable=sv4, state='disabled')
        self.e4.grid(row=4,column=1, sticky = tk.W)
        
        sv5 = tk.StringVar()
        sv5.set(self.user_info["zip_code"])
        sv5.trace("w", lambda name, index, mode, sv=sv5: self.callback())
        self.e5 = tk.Entry(self, textvariable=sv5, state='disabled')
        self.e5.grid(row=5,column=1, sticky = tk.W)
       
        sv6 = tk.StringVar()
        sv6.set(self.user_info["street"])
        sv6.trace("w", lambda name, index, mode, sv=sv6: self.callback())
        self.e6 = tk.Entry(self, textvariable=sv6, state='disabled')
        self.e6.grid(row=6,column=1, sticky = tk.W)
        
       
    def callback(self):
        self.update_button.configure(state="normal")
        
    def create_entry(self,index,r,c):
        t = tk.Entry(self)
        t.grid(row=r,column=c)
        t.insert(0, self.user_info[index])
        return t
    
    def delete_user(self):
        response = messagebox.askyesno("Account Deletion","Are you sure you want to delete you account?")
        if response:
            #delete him and return to login
            instr = "DELETE FROM payment_method where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            instr = "DELETE FROM wallet where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)

            instr = "DELETE FROM support_ticket where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            instr = "DELETE FROM user_buys_subscription_plan where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            instr = "DELETE FROM user_buys_bundle where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr) 
            
            instr = "DELETE FROM user_reviews_service where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr) 
            
            instr = "DELETE FROM user where user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            self.logout()
            
