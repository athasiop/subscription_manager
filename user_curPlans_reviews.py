# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:32:37 2020

@author: Dimitris
"""

import pymysql as sql
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import atexit
import datetime
import re


def reviewPlan(serviceName):
    sqlReviewService = "Select rating from user_reviews_service where user_id = " + str(currUserID) + " and service_name = '" + serviceName + "'"
    cur.execute(sqlReviewService)
    existReview = cur.fetchall()
    existReview = str(existReview).replace('(', '').replace(')', '').replace(",",'')
    if not existReview == "":
        tk.messagebox.showinfo(title = "Already reviewed", message = "You have already reviewed this service. If you want to update your opinion, please double click on" + \
                                  " the review")
    else:
        reviewWindow = tk.Toplevel(userWindow)
        reviewWindow.title(serviceName + " Review")
        reviewWindow.geometry("500x500")
        reviewLabel = tk.Label(reviewWindow,  
              text ="Write your review for " + serviceName + " here")
        reviewText = tk.Text(reviewWindow)
        n = tk.StringVar() 
        cbReviewRating = ttk.Combobox(reviewWindow, width = 10, textvariable =  n, state = 'readonly')
        cbReviewRating['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        btnReview = tk.Button(reviewWindow, text = "Submit Review", 
                               command= lambda: submitReview(serviceName, reviewText, reviewWindow, cbReviewRating))
        reviewLabel.pack()
        reviewText.pack()
        tk.Label(reviewWindow, text = "Rating").pack()
        cbReviewRating.pack()
        btnReview.pack()
        cbReviewRating.current(0)
        reviewWindow.resizable(width=False, height=False)
        reviewWindow.mainloop()
    
            
def submitReview(serviceName, reviewText, reviewWindow, cbReviewRating):
    msgBox = tk.messagebox.askquestion ('Submitting Review','Are you sure you want to submit this review?',icon = 'warning')
    if msgBox == "yes":
        sqlReview = "Insert into user_reviews_service(service_name, user_id, comment, rating, review_date) " + \
        "VALUES ('" + serviceName + "', " + str(currUserID) + ", '" + reviewText.get("1.0", 'end-1c') + "', " + cbReviewRating.get() + ", '" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ "')"
        cur.execute(sqlReview)
        treeReviews.insert("", "end", text = serviceName, values = (cbReviewRating.get(), str(datetime.date.today())))
        reviewWindow.destroy()
    
    
def pop_review_window(dummy_event):
    #data = listReviews.get(listReviews.curselection()[0])
    curReview = treeReviews.focus()
    selectedRow = treeReviews.item(curReview)
    serviceName = str(selectedRow).split(", ")[0]
    serviceName = serviceName[10: -1]
    
    updateReviewWindow = tk.Toplevel(userWindow)
    updateReviewWindow.title("Update review")
    updateReviewWindow.geometry("500x500")
   
    textUpdateReview = tk.Text(updateReviewWindow)
    sqlReviewComment = "Select comment from user_reviews_service where user_id = " + str(currUserID) + " and service_name = '" + serviceName + "'"
    cur.execute(sqlReviewComment)
    resSqlReviewComment = cur.fetchall()
    comment = str(resSqlReviewComment).replace('(', '').replace(')', '').replace(",",'').replace("'", '').replace('"', '')
    textUpdateReview.insert(1.0, comment)
    sqlReviewRating = "Select rating from user_reviews_service where user_id = " + str(currUserID) + " and service_name = '" + serviceName + "'"
    cur.execute(sqlReviewRating)
    resSqlReviewRating = cur.fetchall()
    rating = int(str(resSqlReviewRating).replace('(', '').replace(')', '').replace(",",''))
    btnUpdateReview = tk.Button(updateReviewWindow, text = "Update Review", command = lambda: updateReview(serviceName, textUpdateReview, updateReviewRating, updateReviewWindow))
    btnDeleteReview = tk.Button(updateReviewWindow, text = "Delete Review", command = lambda: deleteReview(serviceName, updateReviewWindow))
    updateReviewRating = ttk.Combobox(updateReviewWindow, width = 10, textvariable =  tk.StringVar, state = 'readonly')    
    updateReviewRating['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    textUpdateReview.pack()
    updateReviewRating.pack()
    btnUpdateReview.pack()
    btnDeleteReview.pack()
    updateReviewRating.current(rating - 1)
    updateReviewWindow.mainloop()
    
def deleteReview(serviceName, updateReviewWindow):
    if tk.messagebox.askquestion(title = "Deleting Review", message = "Are you sure you want to delete this review") == 'yes':
        sqlDeleteReview = "Delete from user_reviews_service where service_name = " + "'" + serviceName + "'"
        cur.execute(sqlDeleteReview)
        cur.execute(sqlReview)
        resSqlReview = cur.fetchall()
        j = 0
        treeReviews.delete(*treeReviews.get_children())
        for x in resSqlReview:
            strX = str(x)
            strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
            strX = strX.split(",")
            treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
            j = j + 1
        updateReviewWindow.destroy()
  
def updateReview(serviceName, textUpdateReview, updateReviewRating, updateReviewWindow):
     if tk.messagebox.askquestion(title = "Updating Review", message = "Are you sure you want to update this review") == 'yes':  
        sqlUpdateReview = "update user_reviews_service set comment = '" + textUpdateReview.get("1.0", 'end-1c')  + "', rating = " + \
        updateReviewRating.get() + " where service_name = '" + serviceName + "'"
        cur.execute(sqlUpdateReview)
        cur.execute(sqlReview)
        resSqlReview = cur.fetchall()
        treeReviews.delete(*treeReviews.get_children())
        j = 0
        for x in resSqlReview:
            strX = str(x)
            strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
            strX = strX.split(",")
            treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
            j = j + 1
        updateReviewWindow.destroy()
    
def checkCancel():
    serviceName = ""
    curReview = treePlans.focus()
    selectedRow = treePlans.item(curReview)
    serviceName = str(selectedRow).split(", ")[0]
    serviceName = serviceName[10: -1] 
    if not serviceName == "":
        cancelPlan(serviceName)
    else:
        tk.messagebox.showerror(title = "Select service", message = "Please select a service to cancel")
  
def cancelPlan(serviceName):
    curReview = treePlans.focus()
    selectedRow = treePlans.item(curReview)
    bundleID = str(selectedRow).split(", ")[5]
    bundleID = bundleID[0 : -1]
    planType = str(selectedRow).split(", ")[3]
    planType = planType[1:]
    print(bundleID)
    if not bundleID == "' '":
        tk.messagebox.showinfo(title = "Canceling from bundle", message = "You cannot cancel a plan that is included in a purchased bundle")
    else:
        if tk.messagebox.askquestion(title = "Canceling plan", message = "Are you sure you want to cancel " + serviceName) == "yes":
            sqlPlanID = "Select user_buys_subscription_plan.plan_id from " + \
            "user_buys_subscription_plan join subscription_plan " +\
            "on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
            "user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
            "where user_id = " + str(currUserID) + " and user_buys_subscription_plan.service_name = '" + serviceName + "'"
            cur.execute(sqlPlanID)
            planID = str(cur.fetchall()).replace('(', '').replace(')', '').replace(",",'')
            sqlCancePlan = "Delete from user_buys_subscription_plan where service_name = '" + serviceName + "'" " and plan_id = '" + planID + "'"
            cur.execute(sqlCancePlan)
            treePlans.delete(*treePlans.get_children())
            sqlPlan = "SELECT subscription_plan.service_name, plan_price, plan_type, plan_purchase_date from " +\
            "user_buys_subscription_plan join subscription_plan " +\
            "on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
            "user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
            "where user_id = " + str(currUserID)
            
            cur.execute(sqlPlan)
            resSqlPlan = cur.fetchall()
            
            i = 1
            for x in resSqlPlan:
                strX = str(x)
                strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                strX = strX.split(",")
                treePlans.insert("", i, text = strX[0], values = (strX[1] + " \u20ac", strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))), " "))
                i = i + 1
            
            sqlBundle = "SELECT bundle_contains_subscription_plan.bundle_id, bundle_contains_subscription_plan.service_name, plan_price, plan_type, bundle_purchase_date from " + \
            "user_buys_bundle join bundle "+ \
            "on user_buys_bundle.bundle_id = bundle.bundle_id " + \
            "join bundle_contains_subscription_plan " + \
            "on bundle.bundle_id = bundle_contains_subscription_plan.bundle_id " + \
            "join subscription_plan "  + \
            "on bundle_contains_subscription_plan.plan_id = subscription_plan.plan_id and " + \
            "bundle_contains_subscription_plan.service_name = subscription_plan.service_name " + \
            "where user_id = " + str(currUserID)
            
            
            cur.execute(sqlBundle)
            resSqlBundle = cur.fetchall()
            
            for x in resSqlBundle:
                strX = str(x)
                strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
                strX = strX.split(",")
                treePlans.insert("", i, text = (strX[1])[1:], values = (strX[2] + " \u20ac", strX[3], str(datetime.date(int(strX[4]), int(strX[5]), int(strX[6]))), strX[0])) # "\u2713"
                i = i + 1
        
def checkReview():
    serviceName = ""
    curReview = treePlans.focus()
    selectedRow = treePlans.item(curReview)
    serviceName = str(selectedRow).split(", ")[0]
    serviceName = serviceName[10: -1] 
    if not serviceName == "":
        reviewPlan(serviceName)
    else:
        tk.messagebox.showerror(title = "Select service", message = "Please select a service to review")
    
userWindow = tk.Tk()
userWindow.geometry("800x800")
    
db = sql.connect("127.0.0.1","user","pass","subscription_manager", autocommit = True)
cur = db.cursor()

    
currUserID = 1;
currUser = ""


treePlans = ttk.Treeview(userWindow)
treePlans["columns"] = ("one","two","three","four")
treePlans.column("#0", width = 150, minwidth = 150, stretch = tk.NO)
treePlans.column("one", width = 50, minwidth = 50, stretch = tk.NO)
treePlans.column("two", width = 80, minwidth = 80)
treePlans.column("three", width = 100, minwidth = 80, stretch = tk.NO)
treePlans.column("four", width = 80, minwidth = 50, stretch = tk.NO)

treePlans.heading("#0",text = "Service",anchor = tk.W)
treePlans.heading("one", text = "Price",anchor = tk.W)
treePlans.heading("two", text = "Type",anchor = tk.W)
treePlans.heading("three", text = "Purchase Date",anchor = tk.W)
treePlans.heading("four", text = "Bundle",anchor = tk.W)

treeReviews = ttk.Treeview(userWindow)
treeReviews["columns"] = ("one","two")
treeReviews.column("#0", width = 150, minwidth = 150, stretch = tk.NO)
treeReviews.column("one", width = 50, minwidth = 50, stretch = tk.NO)
treeReviews.column("two", width = 80, minwidth = 80)

treeReviews.heading("#0",text = "Service",anchor = tk.W)
treeReviews.heading("one", text = "Rating",anchor = tk.W)
treeReviews.heading("two", text = "Review Date",anchor = tk.W)



lblActPlans = tk.Label(userWindow,text = "Active Subscriptions")  
btnReviewPlan = tk.Button(userWindow, text = "Review Service", 
                           command = lambda: checkReview())

lblReviews = tk.Label(userWindow, text = "Reviews (double click to see comment or update review)")

lblActUser = tk.Label(userWindow, text = "")
btnCancelPlan = tk.Button(userWindow, text = "Cancel Plan", command = lambda: checkCancel())


sqlUser = "SELECT user_name, email from user where user_id = " + str(currUserID)
cur.execute(sqlUser)
resSqlUser = cur.fetchall()

for x in resSqlUser:
    strX = str(x)
    strX = strX.replace('(', '').replace(')', '').replace("'",'')
    strX = strX.split(",")
    currUser = strX[0] + strX[1]
    

sqlPlan = "SELECT subscription_plan.service_name, plan_price, plan_type, plan_purchase_date from " +\
"user_buys_subscription_plan join subscription_plan " +\
"on user_buys_subscription_plan.plan_id = subscription_plan.plan_id and " +\
"user_buys_subscription_plan.service_name = subscription_plan.service_name " +\
"where user_id = " + str(currUserID)

cur.execute(sqlPlan)
resSqlPlan = cur.fetchall()

i = 1
for x in resSqlPlan:
    strX = str(x)
    strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
    strX = strX.split(",")
    treePlans.insert("", i, text = strX[0], values = (strX[1] + " \u20ac", strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))), " "))
    i = i + 1

sqlBundle = "SELECT bundle_contains_subscription_plan.bundle_id, bundle_contains_subscription_plan.service_name, plan_price, plan_type, bundle_purchase_date from " + \
"user_buys_bundle join bundle "+ \
"on user_buys_bundle.bundle_id = bundle.bundle_id " + \
"join bundle_contains_subscription_plan " + \
"on bundle.bundle_id = bundle_contains_subscription_plan.bundle_id " + \
"join subscription_plan "  + \
"on bundle_contains_subscription_plan.plan_id = subscription_plan.plan_id and " + \
"bundle_contains_subscription_plan.service_name = subscription_plan.service_name " + \
"where user_id = " + str(currUserID)


cur.execute(sqlBundle)
resSqlBundle = cur.fetchall()

for x in resSqlBundle:
    strX = str(x)
    strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
    strX = strX.split(",")
    treePlans.insert("", i, text = (strX[1])[1:], values = (strX[2] + " \u20ac", strX[3], str(datetime.date(int(strX[4]), int(strX[5]), int(strX[6]))), strX[0])) # "\u2713"
    i = i + 1

sqlReview = "SELECT service_name, comment, rating, review_date FROM user_reviews_service where user_id = " + str(currUserID)
cur.execute(sqlReview)
resSqlReview = cur.fetchall()

j = 1
for x in resSqlReview:
    strX = str(x)
    strX = strX.replace('(', '').replace(')', '').replace("'",'').replace('datetime.datetime', '')
    strX = strX.split(",")
    #listReviews.insert(j, strX[0] + strX[2] + " " + str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5]))))
    treeReviews.insert("", j, text = strX[0], values = (strX[2], str(datetime.date(int(strX[3]), int(strX[4]), int(strX[5])))))
    j = j + 1
    

treeReviews.bind("<Double-Button-1>", pop_review_window)



lblActUser.config(text = currUser)

lblActUser.pack()
lblActPlans.pack()

treePlans.pack()
btnCancelPlan.pack()

btnReviewPlan.pack()
lblReviews.pack()
treeReviews.pack()

userWindow.mainloop()

atexit.register(db.close())