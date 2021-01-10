-To open the app locate the exe file on /User/SubscriptionManagerApplication/SubscriptionManager.exe  
-If that doesn't work you will need to to run the sql files given but also change the ip address from the /User/SubscriptionManager.py to your local connection and run the SubscriptionManager.py file  
-There is also an early build of the company side of the app. Feel free to check it out! (Use "Nietflix" or "Sportifu" as your login credential for the company app)
Known Bug:  
Company app has a column for customer age. Due to the version that was used for mariadb the way we calculated age had syntax errors so we decided to scrap it. That column's values appear to be none for users that were created on the new version of the dump
