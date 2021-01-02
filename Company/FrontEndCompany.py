# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:06:32 2020

@author: Thanasis
"""
import pymysql as sql
from tkinterApp import tkinterApp

company_info = {
    "service_name":""
    }


db = sql.connect("127.0.0.1","company","comp","subscription_manager",autocommit=True)
cur = db.cursor()  

app = tkinterApp(cur,company_info)
app.mainloop()
db.close()