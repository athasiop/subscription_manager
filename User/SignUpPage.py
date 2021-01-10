import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from MainMenu import MainMenu

class SignUpPage(tk.Frame):
    
    def __init__(self,parent,cur,user_info,frames, loginWindow):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.user_info=user_info
        self.frames = frames
        self.loginWindow = loginWindow
          
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e2.insert(tk.END, "year/month/day")
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)
        self.e5 = tk.Entry(self)
        self.e6 = tk.Entry(self)
        
        
        
        tk.Label(self,text="Username").pack()
        self.e1.pack()
        tk.Label(self,text="Birth Date").pack()
        self.e2.pack()
        tk.Label(self,text="Email").pack()
        self.e3.pack()
        tk.Label(self,text="Country").pack()
        self.e4.pack()
        tk.Label(self,text="Zip Code").pack()
        self.e5.pack()
        tk.Label(self,text="Street").pack()
        self.e6.pack()
        
        
     
        imgSize = 25, 25
        imgLogin = Image.open(r"Images\back.png")
        imgSignUp = Image.open("Images\signup.png")
        
        newImgLogin = imgLogin.resize(imgSize) 
        newImgSignUp = imgSignUp.resize(imgSize)
        self.photoLogin = ImageTk.PhotoImage(newImgLogin)
        self.photoSignUp = ImageTk.PhotoImage(newImgSignUp)
        login_button = ttk.Button(self,text="Back", image = self.photoLogin, compound = tk.RIGHT, command=self.login)
        login_button.pack(pady = 25)
        
        sign_up_button = ttk.Button(self,text="Sign Up", image = self.photoSignUp, compound = tk.RIGHT, command = self.sign_up)
        sign_up_button.pack()
    def clear(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        
    def login(self):
        frame = self.frames["LoginPage"]
        frame.tkraise()
    def sign_up(self):
        self.user_info["user_name"] = str(self.e1.get())
        self.user_info["birth_date"] = str(self.e2.get())
        self.user_info["email"] = str(self.e3.get())
        self.user_info["country"] = str(self.e4.get())
        self.user_info["zip_code"] = str(self.e5.get())
        self.user_info["street"] = str(self.e6.get())
        strcheck = self.user_info["birth_date"]
        
        instr = "INSERT INTO user (user_name,email,country,birth_date,zip_code,street) VALUES ('"+self.user_info.get("user_name")+"','"+self.user_info.get("email")+"','"+self.user_info.get("country")+"','"+self.user_info.get("birth_date")+"','"+ self.user_info.get("zip_code")+"','"+self.user_info.get("street")+"')"
        try:
            self.cur.execute(instr)
            try:
                info = "SELECT user_id FROM user WHERE user_name='"+self.user_info["user_name"]+"' AND email='"+self.user_info["email"]+"'"       
                self.cur.execute(info)
                record = self.cur.fetchone()
                self.user_info["user_id"]=record[0]               
                instr = "INSERT INTO wallet (user_id,money) VALUES ("+str(self.user_info["user_id"])+",0)"                
                self.cur.execute(instr)                
            except:
                print("Can't find user_id")
            self.loginWindow.withdraw()
            self.loginWindow.show_frame("LoginPage")
            mainWindow = MainMenu(self.cur, self.user_info, self.loginWindow)
            mainWindow.mainloop()
        except:
            if len(strcheck)<8:
                self.user_not_found_label = tk.Label(self,text="Wrong birth date format.\n Correct example:1992/9/21",bg="firebrick1")
                self.user_not_found_label.pack()
                
                self.after(5000, self.clear_label)
            elif (not (strcheck[4]=="/" or strcheck[4]=="-")):           
                self.user_not_found_label = tk.Label(self,text="Wrong birth date format.\n Correct example:1992/9/21",bg="firebrick1")
                self.user_not_found_label.pack()
                self.after(5000, self.clear_label)
            else:
                self.user_not_found_label = tk.Label(self,text="Wrong credentials were inserted.\n Username and/or Email already exist!",bg="firebrick1")
                self.user_not_found_label.pack()
                self.after(5000, self.clear_label)                
            print("invalid input")
    def clear_label(self):
        self.user_not_found_label.pack_forget()
    
        