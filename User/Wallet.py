import tkinter as tk
from createToolbar import createToolbar
from PIL import Image, ImageTk

class Wallet(tk.Frame):    
    def __init__(self,parent,cur,user_info,frames,loginWindow,mainWindow):         
        tk.Frame.__init__(self, parent)        
        self.user_info = user_info
        self.cur = cur
        self.frames = frames
        self.loginWindow = loginWindow
        self.mainWindow = mainWindow
        
        imgSize = 30, 30
        imgAddMoney = Image.open(r"Images\addMoney.png")
        imgPayment= Image.open(r"Images\payment.png")
        #imgPaymentMethods = Image.open(r"Images\paymentMethods.png")
        newImgAddMoney = imgAddMoney.resize(imgSize)
        newImgPayment= imgPayment.resize(imgSize)
        #newImgPaymentMethods = imgPaymentMethods.resize((360, 180))
        self.photoAddMoney = ImageTk.PhotoImage(newImgAddMoney)
        self.photoPayment = ImageTk.PhotoImage(newImgPayment)
        #self.photoPaymenMethods = ImageTk.PhotoImage(newImgPaymentMethods)
        
        createToolbar(self, frames)
        # label=tk.Label(self, text="MAIN MENU")
        # label.grid(row=0, column=1,pady=10, padx=10)
        add_money_button=tk.Button(self, text="Add Money", image = self.photoAddMoney, compound = tk.RIGHT, command=lambda: self.addMoney())
        add_money_button.grid(row=1, column=1,pady=10, padx=10)
        payment_method_button=tk.Button(self, text="Payment Methods", image = self.photoPayment, compound = tk.RIGHT,command=lambda: self.show_PM())
        payment_method_button.grid(row=2, column=1,pady=10, padx=10)
        # buy_plan_button=tk.Button(self, text="Buy Plans", command=lambda: self.show_buyPlan())
        # buy_plan_button.grid(row=3,column=1,pady=10,padx=10)
        
        

    def show_PM(self):
        frame=self.frames["PaymentMethod"]
        frame.tkraise()
        
    def show(self):
        try:
            instr="SELECT * FROM wallet WHERE user_id="+str(self.user_info["user_id"])
            self.cur.execute(instr)
            
            record = self.cur.fetchone()
        except:
            print("User Not Found!")
        
        tk.Label(self,text="You have " + str(record[0]) + "€ in your account").grid(row=1, column=3)
        
    def addMoney(self):
        frame=self.frames["WalletPage"]
        frame.tkraise()
#TOOLBAR        
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
        frame.RefreshProfile()
        frame.tkraise()