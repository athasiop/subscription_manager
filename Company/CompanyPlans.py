import tkinter as tk
from tkinter import ttk
import math


class CompanyPlans(tk.Frame):
    def __init__(self, parent, cur, company_info, frames):
        tk.Frame.__init__(self, parent)
        self.company_info = company_info
        self.frames = frames
        self.cur = cur
        
    
        self.treePlans = tk.ttk.Treeview(self)
        self.treePlans["columns"] = ("one","two", "three", "four")
        self.treePlans.column("#0", width = 80, minwidth = 50, stretch = tk.NO)
        self.treePlans.column("one", width = 100, minwidth = 100, stretch = tk.NO)
        self.treePlans.column("two", width = 80, minwidth = 80, stretch = tk.NO)
        self.treePlans.column("three", width = 80, minwidth = 80, stretch = tk.NO)
        self.treePlans.column("four", width = 80, minwidth = 80, stretch = tk.NO)
        
        
        self.treePlans.heading("#0", text = "",anchor = tk.W)
        self.treePlans.heading("one", text = "Price",anchor = tk.W)
        self.treePlans.heading("two", text = "Type",anchor = tk.W)
        self.treePlans.heading("three", text = "Region",anchor = tk.W)
        self.treePlans.heading("four", text = "Current Users", anchor = tk.W)
        ttk.Button(self,text="Show Reviews",command = self.show_reviews).grid(row=1,column=1)
    def show_info(self):
        
        self.treePlans.delete(*self.treePlans.get_children())
        tk.Label(self, text = "Hello " + self.company_info["service_name"] + "! Your offered plans are:\n (Double click if you want to update your plan). " ).grid(row = 0, column = 0, sticky="nsew")
        self.treePlans.grid(row=1,column=0,sticky="nsew") 
        lblWarning = tk.Label(self, text = "Plan's deletion is not feasible from the menu. \n Please let us know if you want to delete a plan. ")
        lblWarning.grid(row = 2, column = 0, stick = "nsew")
        lblWarning.configure(foreground="red")
        
        sqlServicePlans = "Select * from subscription_plan where service_name = '" + self.company_info["service_name"] + "'"
        self.cur.execute(sqlServicePlans)
        resSqlServicePlans = self.cur.fetchall()
        
        
        j = 1
        for x in resSqlServicePlans:
            strX = str(x)
            strX = strX.replace("(", "").replace(")", "").replace("'", "")
            strX = strX.split(",")
            sqlNumOfUsersPlans = "select count(user_id) from subscription_plan join user_buys_subscription_plan " + \
            "on subscription_plan.plan_id = user_buys_subscription_plan.plan_id " +\
            "and subscription_plan.service_name = user_buys_subscription_plan.service_name " + \
            "where subscription_plan.service_name = '" + self.company_info["service_name"] + "' and subscription_plan.plan_id = " + strX[0]
            self.cur.execute(sqlNumOfUsersPlans)
            resSqlCurNumOfUsersPlans = self.cur.fetchone()
            currUserPlans = str(resSqlCurNumOfUsersPlans).replace("(", "").replace(")", "").replace(",", "")
            self.treePlans.insert("", j, text = strX[0] , values = (strX[1] + " \u20ac", strX[3], strX[2], currUserPlans))
            j = j + 1
        
        
        sqlCurNumUsers = "select count(user_id) from subscription_plan join user_buys_subscription_plan " + \
        "on subscription_plan.plan_id = user_buys_subscription_plan.plan_id " + \
        "and subscription_plan.service_name = user_buys_subscription_plan.service_name " + \
        "where subscription_plan.service_name = '" + self.company_info["service_name"] + "'" 
        self.cur.execute(sqlCurNumUsers)
        resSqlCurNumUsers = self.cur.fetchone()
        strX = str(resSqlCurNumUsers).replace("(", "").replace(")", "").replace(",", "")
        tk.Label(self, text = "Total Current Users: " + strX).grid(row = 0, column = 1, stick = "nsew")
        self.treePlans.bind("<Double-Button-1>", self.pop_update_window)

    def show_reviews(self):
        frame = self.frames["ReviewsPage"]
        frame.RefreshList()
        frame.tkraise()
     
    def pop_update_window(self, dummy_event):
        curPlan = self.treePlans.focus()
        selectedRow = self.treePlans.item(curPlan)
        splitRow = str(selectedRow).split(", ")
        selectPlanID = splitRow[0]
        selectPlanID = selectPlanID[10:-1]
        selectPrice = splitRow[2]
        selectPrice = selectPrice[13:-2]
        selectType = splitRow[3]
        selectRegion = splitRow[4]
        selectRegion = selectRegion[2:].replace("'", "")
        selectType = selectType[2:].replace("'", "")
        
        updatePlanWindow = tk.Toplevel(self)
        updatePlanWindow.title("Update review")
        updatePlanWindow.geometry("600x500")
        textUpdatePrice = tk.Text(updatePlanWindow, width = 10, height = 1)
        textUpdatePrice.insert(1.0, selectPrice)

        textUpdateType = tk.Text(updatePlanWindow, width = 10, height = 1)
        textUpdateType.insert(1.0, selectType)
        textUpdateRegion = tk.Text(updatePlanWindow, width = 15, height = 1)
        textUpdateRegion.insert(1.0, selectRegion)
        tk.Label(updatePlanWindow, text = "Price = ").grid(row = 1, column = 0)
        tk.Label(updatePlanWindow, text = "Type = ").grid(row = 3, column = 0)
        tk.Label(updatePlanWindow, text = "Region = ").grid(row = 5, column = 0)
        tk.Button(updatePlanWindow, text = "Update Plan", command = lambda: self.updatePlan(textUpdatePrice, textUpdateType, textUpdateRegion, selectPlanID, updatePlanWindow)).grid(row = 6, column = 1)
        textUpdatePrice.grid(row = 1, column = 1 , stick = "nsew")
        textUpdateType.grid(row = 3, column = 1, stick = "nsew")
        textUpdateRegion.grid(row = 5, column = 1, stick = "nsew")
        
        tvUserInfo = tk.ttk.Treeview(updatePlanWindow)
        tvUserInfo["columns"] = ("one", "two")
        tvUserInfo.column("#0", width = 200, minwidth = 50, stretch = tk.NO)
        tvUserInfo.column("one", width = 200, minwidth = 100, stretch = tk.NO)
        tvUserInfo.column("two", width = 50, minwidth = 50, stretch = tk.NO)

        
        
        tvUserInfo.heading("#0", text = "Name",anchor = tk.W)
        tvUserInfo.heading("one", text = "Email",anchor = tk.W)
        tvUserInfo.heading("two", text = "Age",anchor = tk.W)
        
        tk.Label(updatePlanWindow, text = "Users").grid(row = 7, column = 1)
        tvUserInfo.grid(row=8,column=1,sticky="nsew")
        
        sqlUserHasPlan = "select user_name, email, age from subscription_plan join user_buys_subscription_plan " + \
        "on subscription_plan.plan_id = user_buys_subscription_plan.plan_id " + \
        "and subscription_plan.service_name = user_buys_subscription_plan.service_name " + \
        "join user on user.user_id = user_buys_subscription_plan.user_id " + \
        "where subscription_plan.service_name = '" + self.company_info["service_name"] + "' and subscription_plan.plan_id = " + selectPlanID
        self.cur.execute(sqlUserHasPlan)
        resSqlUserHasPlan = self.cur.fetchall()
        resSqlUserHasPlan = str(resSqlUserHasPlan).replace("(", "").replace(")", "").replace("'", "").split(",")
        c = 0
        if not (len(resSqlUserHasPlan) == 4):
            for i in range(0, math.ceil(len(resSqlUserHasPlan)/2), 1):
                if not i == 0:
                    resSqlUserHasPlan[c] = (resSqlUserHasPlan[c])[1:]
                tvUserInfo.insert("", i, text = resSqlUserHasPlan[c], values = (resSqlUserHasPlan[c+1], resSqlUserHasPlan[c+2]))
                c = c + 3
        else:
             tvUserInfo.insert("", 1, text = resSqlUserHasPlan[0], values = (resSqlUserHasPlan[1], resSqlUserHasPlan[2]))
        updatePlanWindow.resizable(width=False, height=False)
        updatePlanWindow.mainloop()
        
    def updatePlan(self, textUpdatePrice, textUpdateType, textUpdateRegion, selectPlanID, updatePlanWindow):        
        if tk.messagebox.askquestion(title = "Updating Plan", message = "Are you sure you want to update this plan") == 'yes':  
                sqlUpdatePlan= "update subscription_plan set plan_price = " + textUpdatePrice.get("1.0", 'end-1c')  + ", plan_type = '" + \
                textUpdateType.get("1.0", 'end-1c') + "', region = '" + textUpdateRegion.get("1.0", 'end-1c') +  "' where service_name = '" + self.company_info["service_name"] + "' " +\
                "and plan_id = " + selectPlanID
                self.cur.execute(sqlUpdatePlan)
                self.treePlans.delete(*self.treePlans.get_children())
                sqlServicePlans = "Select * from subscription_plan where service_name = '" + self.company_info["service_name"] + "'"
                self.cur.execute(sqlServicePlans)
                resSqlServicePlans = self.cur.fetchall()
                               
                j = 1
                for x in resSqlServicePlans:
                    strX = str(x)
                    strX = strX.replace("(", "").replace(")", "").replace("'", "")
                    strX = strX.split(",")
                    sqlNumOfUsersPlans = "select count(user_id) from subscription_plan join user_buys_subscription_plan " + \
                    "on subscription_plan.plan_id = user_buys_subscription_plan.plan_id " +\
                    "and subscription_plan.service_name = user_buys_subscription_plan.service_name " + \
                    "where subscription_plan.service_name = '" + self.company_info["service_name"] + "' and subscription_plan.plan_id = " + strX[0]
                    self.cur.execute(sqlNumOfUsersPlans)
                    resSqlCurNumOfUsersPlans = self.cur.fetchone()
                    currUserPlans = str(resSqlCurNumOfUsersPlans).replace("(", "").replace(")", "").replace(",", "")
                    self.treePlans.insert("", j, text = strX[0] , values = (strX[1] + " \u20ac", strX[3], strX[2], currUserPlans))
                    j = j + 1
        
        
                sqlCurNumUsers = "select count(user_id) from subscription_plan join user_buys_subscription_plan " + \
                "on subscription_plan.plan_id = user_buys_subscription_plan.plan_id " + \
                "and subscription_plan.service_name = user_buys_subscription_plan.service_name " + \
                "where subscription_plan.service_name = '" + self.company_info["service_name"] + "'" 
                self.cur.execute(sqlCurNumUsers)
                resSqlCurNumUsers = self.cur.fetchone()
                strX = str(resSqlCurNumUsers).replace("(", "").replace(")", "").replace(",", "")
                tk.Label(self, text = "Current Users: " + strX).grid(row = 0, column = 1, stick = "nsew")
                self.treePlans.bind("<Double-Button-1>", self.pop_update_window)
                
                updatePlanWindow.destroy()