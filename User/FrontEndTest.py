import pymysql as sql
from tkinterApp import tkinterApp


user_info = {
    "user_id":"",
    "user_name":"",
    "birth_date":"",
    "email":"",
    "country":"",
    "zip_code":"",
    "street":""
    }

db = sql.connect("127.0.0.1","user","pass","subscription_manager",autocommit=True) #46.12.85.152
cur = db.cursor()  


app = tkinterApp(cur,user_info)
app.mainloop()
db.close()