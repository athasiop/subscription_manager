import pymysql as sql
from tkinterApp import tkinterApp

company_info = {
    "service_name":""
    }


db = sql.connect("34.107.12.9","company","comp","subscription_manager",autocommit=True)
cur = db.cursor()  

app = tkinterApp(cur,company_info)
app.mainloop()
db.close()