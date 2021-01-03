# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:32:37 2020

@author: Thanasaras
"""


import datetime
import tkinter as tk
from createToolbar import createToolbar
from tkinter import ttk
from PIL import Image, ImageTk



    

        
class CurrentPlans(tk.Frame):
        def __init__(self, parent, cur, user_info, frames):
            tk.Frame.__init__(self, parent)
            self.user_info = user_info
            self.frames = frames
            self.cur = cur
            
            imgSize = 20, 20
            imgCancel = Image.open("cancel.png")
            imgReview = Image.open("review.png")
            newImgCancel = imgCancel.resize(imgSize) 
            newImgReview = imgReview.resize(imgSize)
            self.photoCancel = ImageTk.PhotoImage(newImgCancel)
            self.photoReview = ImageTk.PhotoImage(newImgReview)
            
            self.treePlans = ttk.Treeview(self)
            self.treePlans["columns"] = ("one","two","three","four")
            self.treePlans.column("#0", width = 150, minwidth = 150, stretch = tk.NO)
            self.treePlans.column("one", width = 50, minwidth = 50, stretch = tk.NO)
            self.treePlans.column("two", width = 80, minwidth = 80)
            self.treePlans.column("three", width = 100, minwidth = 80, stretch = tk.NO)
            self.treePlans.column("four", width = 80, minwidth = 50, stretch = tk.NO)
            
            self.treePlans.heading("#0", text = "Service",anchor = tk.W)
            self.treePlans.heading("one", text = "Price",anchor = tk.W)
            self.treePlans.heading("two", text = "Type",anchor = tk.W)
            self.treePlans.heading("three", text = "Purchase Date",anchor = tk.W)
            self.treePlans.heading("four", text = "Bundle",anchor = tk.W)
            
            self.treeReviews = ttk.Treeview(self)
            self.treeReviews["columns"] = ("one","two")
            self.treeReviews.column("#0", width = 150, minwidth = 150, stretch = tk.NO)
            self.treeReviews.column("one", width = 50, minwidth = 50, stretch = tk.NO)
            self.treeReviews.column("two", width = 80, minwidth = 80)
            
            self.treeReviews.heading("#0",text = "Service",anchor = tk.W)
            self.treeReviews.heading("one", text = "Rating",anchor = tk.W)
            self.treeReviews.heading("two", text = "Review Date",anchor = tk.W)
            
            
         
            self.lblActPlans = tk.Label(self, text = "Active Subscriptions")  
            self.btnReviewPlan = tk.Button(self, text = "Review Service", image = self.photoReview, compound = tk.RIGHT,
                                       command = lambda: self.checkReview())
            
            self.lblReviews = tk.Label(self, text = "Reviews (double click to see comment or update review)")
            
            
            self.btnCancelPlan = tk.Button(self, text = "Cancel Plan", image = self.photoCancel, compound = tk.RIGHT, command = lambda: self.checkCancel())
            
            self.treeReviews.bind("<Double-Button-1>", self.pop_review_window)
        
            
            self.lblActPlans.grid(row = 1, column = 0, stick = "nsew")
            
            self.treePlans.grid(row = 2, column = 0, stick = "nsew")
            self.btnCancelPlan.grid(row = 3, column = 0)
            
            self.btnReviewPlan.grid(row = 4, column = 0)
            self.lblReviews.grid(row = 1, column = 2, stick = "nsew")
            self.treeReviews.grid(row = 2, column = 2, stick = "nsew")
            
            createToolbar(self, frames)
            
        def show(self):
            
            sqlPlan = "SELECT subscription_plan.service_name, plan_price, plan_type, plan_purchase_date from " +\
            "user_buys_subscription_plan join subscription_plan " +\
            "on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
            "user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
            "where user_id = " + str(self.user_info["user_id"])
            
            self.cur.execute(sqlPlan)
            resSqlPlan = self.cur.fetchall()
            
            i = 1
            for x in resSqlPlan:
                strX = str(x)
                strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                strX = strX.split(",")
                self.treePlans.insert("", i, text = strX[0], values = (strX[1] + " \u20ac", strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))), " "))
                i = i + 1
            
            sqlBundle = "SELECT bundle_contains_subscription_plan.bundle_id, bundle_contains_subscription_plan.service_name, plan_price, plan_type, bundle_purchase_date from " + \
            "user_buys_bundle join bundle "+ \
            "on user_buys_bundle.bundle_id = bundle.bundle_id " + \
            "join bundle_contains_subscription_plan " + \
            "on bundle.bundle_id = bundle_contains_subscription_plan.bundle_id " + \
            "join subscription_plan "  + \
            "on bundle_contains_subscription_plan.plan_id = subscription_plan.plan_id and " + \
            "bundle_contains_subscription_plan.service_name = subscription_plan.service_name " + \
            "where user_id = " + str(self.user_info["user_id"])
            
            
            self.cur.execute(sqlBundle)
            resSqlBundle = self.cur.fetchall()
            
            for x in resSqlBundle:
                strX = str(x)
                strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                strX = strX.split(",")
                self.treePlans.insert("", i, text = (strX[1])[1:], values = (strX[2] + " \u20ac", strX[3], str(datetime.date(int(strX[4]), int(strX[5]), int(strX[6]))), strX[0])) # "\u2713"
                i = i + 1
        
            sqlReview = "SELECT service_name, comment, rating, review_date FROM user_reviews_service where user_id = " + str(self.user_info["user_id"])
            self.cur.execute(sqlReview)
            resSqlReview = self.cur.fetchall()
            
            j = 1
            for x in resSqlReview:
                strX = str(x)
                strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                strX = strX.split(",")
                #listReviews.insert(j, strX[0] + strX[2] + " " + str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))))
                self.treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
                j = j + 1
                
            
            

        def reviewPlan(self, serviceName):
            sqlReviewService = "Select rating from user_reviews_service where user_id = " + str(self.user_info["user_id"]) + " and service_name = '" + serviceName + "'"
            self.cur.execute(sqlReviewService)
            existReview = self.cur.fetchall()
            existReview = str(existReview).replace('(', '').replace(')', '').replace(",",'')
            if not existReview == "":
                tk.messagebox.showinfo(title = "Already reviewed", message = "You have already reviewed this service. If you want to update your opinion, please double click on" + \
                                          " the review")
            else:
                reviewWindow = tk.Toplevel(self)
                reviewWindow.title(serviceName + " Review")
                reviewWindow.geometry("500x500")
                reviewLabel = tk.Label(reviewWindow,  
                      text ="Write your review for " + serviceName + " here")
                reviewText = tk.Text(reviewWindow)
                n = tk.StringVar() 
                cbReviewRating = ttk.Combobox(reviewWindow, width = 10, textvariable =  n, state = 'readonly')
                cbReviewRating['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                btnReview = tk.Button(reviewWindow, text = "Submit Review", 
                                       command= lambda: self.submitReview(serviceName, reviewText, reviewWindow, cbReviewRating))
                reviewLabel.pack()
                reviewText.pack()
                tk.Label(reviewWindow, text = "Rating").pack()
                cbReviewRating.pack()
                btnReview.pack()
                cbReviewRating.current(0)
                reviewWindow.resizable(width=False, height=False)
                reviewWindow.mainloop()
            
                    
        def submitReview(self, serviceName, reviewText, reviewWindow, cbReviewRating):
            msgBox = tk.messagebox.askquestion ('Submitting Review','Are you sure you want to submit this review?',icon = 'warning')
            if msgBox == "yes":
                sqlReview = "Insert into user_reviews_service(service_name, user_id, comment, rating, review_date) " + \
                "VALUES ('" + serviceName + "', " + str(self.user_info["user_id"]) + ", '" + reviewText.get("1.0", 'end-1c') + "', " + cbReviewRating.get() + ", '" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ "')"
                self.cur.execute(sqlReview)
                self.treeReviews.insert("", "end", text = serviceName, values = (cbReviewRating.get(), str(datetime.date.today())))
                reviewWindow.destroy()
            
            
        def pop_review_window(self, dummy_event):
            #data = listReviews.get(listReviews.curselection()[0])
            curReview = self.treeReviews.focus()
            selectedRow = self.treeReviews.item(curReview)
            serviceName = str(selectedRow).split(", ")[0]
            serviceName = serviceName[10: -1]
            
            updateReviewWindow = tk.Toplevel(self)
            updateReviewWindow.title("Update review")
            updateReviewWindow.geometry("500x500")
           
            textUpdateReview = tk.Text(updateReviewWindow)
            sqlReviewComment = "Select comment from user_reviews_service where user_id = " + str(self.user_info["user_id"]) + " and service_name = '" + serviceName + "'"
            self.cur.execute(sqlReviewComment)
            resSqlReviewComment = self.cur.fetchall()
            comment = str(resSqlReviewComment).replace('(', '').replace(')', '').replace(",",'').replace("'", '').replace('"', '')
            textUpdateReview.insert(1.0, comment)
            sqlReviewRating = "Select rating from user_reviews_service where user_id = " + str(self.user_info["user_id"]) + " and service_name = '" + serviceName + "'"
            self.cur.execute(sqlReviewRating)
            resSqlReviewRating = self.cur.fetchall()
            rating = int(str(resSqlReviewRating).replace('(', '').replace(')', '').replace(",",''))
            btnUpdateReview = tk.Button(updateReviewWindow, text = "Update Review", command = lambda: self.updateReview(serviceName, textUpdateReview, updateReviewRating, updateReviewWindow))
            btnDeleteReview = tk.Button(updateReviewWindow, text = "Delete Review", command = lambda: self.deleteReview(serviceName, updateReviewWindow))
            updateReviewRating = ttk.Combobox(updateReviewWindow, width = 10, textvariable =  tk.StringVar, state = 'readonly')    
            updateReviewRating['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            textUpdateReview.pack()
            updateReviewRating.pack()
            btnUpdateReview.pack()
            btnDeleteReview.pack()
            updateReviewRating.current(rating - 1)
            updateReviewWindow.mainloop()
            
        def deleteReview(self, serviceName, updateReviewWindow):
            if tk.messagebox.askquestion(title = "Deleting Review", message = "Are you sure you want to delete this review") == 'yes':
                sqlDeleteReview = "Delete from user_reviews_service where service_name = " + "'" + serviceName + "'"
                self.cur.execute(sqlDeleteReview)
                sqlReview = "SELECT service_name, comment, rating, review_date FROM user_reviews_service where user_id = " + str(self.user_info["user_id"])
                self.cur.execute(sqlReview)
                resSqlReview = self.cur.fetchall()
                j = 0
                self.treeReviews.delete(*self.treeReviews.get_children())
                for x in resSqlReview:
                    strX = str(x)
                    strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                    strX = strX.split(",")
                    self.treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
                    j = j + 1
                updateReviewWindow.destroy()
          
        def updateReview(self, serviceName, textUpdateReview, updateReviewRating, updateReviewWindow):
             if tk.messagebox.askquestion(title = "Updating Review", message = "Are you sure you want to update this review") == 'yes':  
                sqlUpdateReview = "update user_reviews_service set comment = '" + textUpdateReview.get("1.0", 'end-1c')  + "', rating = " + \
                updateReviewRating.get() + " where service_name = '" + serviceName + "'"
                self.cur.execute(sqlUpdateReview)
                sqlReview = "SELECT service_name, comment, rating, review_date FROM user_reviews_service where user_id = " + str(self.user_info["user_id"])
                self.cur.execute(sqlReview)
                resSqlReview = self.cur.fetchall()
                self.treeReviews.delete(*self.treeReviews.get_children())
                j = 0
                for x in resSqlReview:
                    strX = str(x)
                    strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                    strX = strX.split(",")
                    self.treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
                    j = j + 1
                updateReviewWindow.destroy()
            
        def checkCancel(self):
            serviceName = ""
            curReview = self.treePlans.focus()
            selectedRow = self.treePlans.item(curReview)
            serviceName = str(selectedRow).split(", ")[0]
            serviceName = serviceName[10: -1] 
            if not serviceName == "":
                self.cancelPlan(serviceName)
            else:
                tk.messagebox.showerror(title = "Select service", message = "Please select a service to cancel")
          
        def cancelPlan(self, serviceName):
            curReview = self.treePlans.focus()
            selectedRow = self.treePlans.item(curReview)
            bundleID = str(selectedRow).split(", ")[5]
            bundleID = bundleID[0 : -1]
            planType = str(selectedRow).split(", ")[3]
            planType = planType[1:]
            print(bundleID)
            if not bundleID == "' '":
                tk.messagebox.showinfo(title = "Canceling from bundle", message = "You cannot cancel a plan that was included in a purchased bundle")
            else:
                if tk.messagebox.askquestion(title = "Canceling plan", message = "Are you sure you want to cancel " + serviceName) == "yes":
                    sqlPlanID = "Select user_buys_subscription_plan.plan_id from " + \
                    "user_buys_subscription_plan join subscription_plan " +\
                    "on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
                    "user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
                    "where user_id = " + str(self.user_info["user_id"]) + " and user_buys_subscription_plan.service_name = '" + serviceName + "'"
                    self.cur.execute(sqlPlanID)
                    planID = str(self.cur.fetchall()).replace('(', '').replace(')', '').replace(",",'')
                    sqlCancePlan = "Delete from user_buys_subscription_plan where service_name = '" + serviceName + "'" " and plan_id = '" + planID + "'"
                    self.cur.execute(sqlCancePlan)
                    self.treePlans.delete(*self.treePlans.get_children())
                    sqlPlan = "SELECT subscription_plan.service_name, plan_price, plan_type, plan_purchase_date from " +\
                    "user_buys_subscription_plan join subscription_plan " +\
                    "on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
                    "user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
                    "where user_id = " + str(self.user_info["user_id"])
                    
                    self.cur.execute(sqlPlan)
                    resSqlPlan = self.cur.fetchall()
                    
                    i = 1
                    for x in resSqlPlan:
                        strX = str(x)
                        strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                        strX = strX.split(",")
                        self.treePlans.insert("", i, text = strX[0], values = (strX[1] + " \u20ac", strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))), " "))
                        i = i + 1
                    
                    sqlBundle = "SELECT bundle_contains_subscription_plan.bundle_id, bundle_contains_subscription_plan.service_name, plan_price, plan_type, bundle_purchase_date from " + \
                    "user_buys_bundle join bundle "+ \
                    "on user_buys_bundle.bundle_id = bundle.bundle_id " + \
                    "join bundle_contains_subscription_plan " + \
                    "on bundle.bundle_id = bundle_contains_subscription_plan.bundle_id " + \
                    "join subscription_plan "  + \
                    "on bundle_contains_subscription_plan.plan_id = subscription_plan.plan_id and " + \
                    "bundle_contains_subscription_plan.service_name = subscription_plan.service_name " + \
                    "where user_id = " + str(self.user_info["user_id"])
                    
                    
                    self.cur.execute(sqlBundle)
                    resSqlBundle = self.cur.fetchall()
                    
                    for x in resSqlBundle:
                        strX = str(x)
                        strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                        strX = strX.split(",")
                        self.treePlans.insert("", i, text = (strX[1])[1:], values = (strX[2] + " \u20ac", strX[3], str(datetime.date(int(strX[4]), int(strX[5]), int(strX[6]))), strX[0])) # "\u2713"
                        i = i + 1
                
        def checkReview(self):
            serviceName = ""
            curReview = self.treePlans.focus()
            selectedRow = self.treePlans.item(curReview)
            serviceName = str(selectedRow).split(", ")[0]
            serviceName = serviceName[10: -1] 
            if not serviceName == "":
                self.reviewPlan(serviceName)
            else:
                tk.messagebox.showerror(title = "Select service", message = "Please select a service to review")
        
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



    
