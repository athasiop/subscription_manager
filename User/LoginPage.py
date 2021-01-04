import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from MainMenu import MainMenu

class LoginPage(tk.Frame):
    
    def __init__(self,parent,cur,user_info,frames, loginWindow):
        tk.Frame.__init__(self, parent)
        self.cur = cur
        self.user_info=user_info
        self.frames = frames
        self.loginWindow = loginWindow
        
        imgSize = 25, 25
        imgLogin = Image.open("Images\login.png")
        imgSignUp = Image.open("Images\signup.png")
        imgServices = Image.open("Images\services.jpg")
        
        newImgLogin = imgLogin.resize(imgSize) 
        newImgSignUp = imgSignUp.resize(imgSize)
        newImgServices = imgServices.resize((350,200))
        self.photoLogin = ImageTk.PhotoImage(newImgLogin)
        self.photoSignUp = ImageTk.PhotoImage(newImgSignUp)
        self.photoServices = ImageTk.PhotoImage(newImgServices)
        
        tk.Label(self, text = "Subscription Manager", font='Helvetica 12 bold').pack(pady = 5)
        tk.Label(self,image = self.photoServices).pack()
        tk.Label(self,text = "Username").place(x = 50, y = 250)
        entry_username = tk.Entry(self)
        entry_username.place(x = 120, y = 250)
        
        tk.Label(self,text = "Email").place(x = 50, y = 280)
        entry_email = tk.Entry(self)
        entry_email.place(x = 120, y = 280)
        
        login_button = ttk.Button(self,text="Log In", image = self.photoLogin, compound = tk.RIGHT, command=lambda:self.login(str(entry_username.get()),str(entry_email.get())))
        login_button.place(x = 260, y = 258)
        
        sign_up_button = ttk.Button(self,text="Sign Up", image = self.photoSignUp, compound = tk.RIGHT, command = lambda:self.sign_up())
        sign_up_button.place(x = 140, y = 330)
        
        
    def login(self,username,email):
        try:
            instr = "SELECT * FROM user WHERE user_name='"+username+"' AND email='"+email+"'"
            
            self.cur.execute(instr)
            record = self.cur.fetchone()
            self.user_info["user_id"]=record[0]
            self.user_info["user_name"] =  record[1]
            self.user_info["birth_date"] =  record[2]
            self.user_info["email"] =  record[4]
            self.user_info["country"] =  record[5]
            self.user_info["zip_code"] =  record[6]
            self.user_info["street"] =  record[7]

            
            self.loginWindow.withdraw()
            mainWindow = MainMenu(self.cur, self.user_info, self.loginWindow)
            mainWindow.mainloop()
        except tk.TclError as e:
            print("Issue with tinker: "+str(e))
        except Exception as e:
            self.user_not_found_label = tk.Label(self,text="User Not Found",bg="firebrick1")
            self.user_not_found_label.place(x = 150, y = 305)
            self.after(3000, self.user_not_found_label.destroy)
            print("Error: "+str(e))
    def clear_label(self):
        self.user_not_found_label.grid_forget()
    def sign_up(self):
        frame = self.frames["SignUpPage"]
        frame.tkraise()    