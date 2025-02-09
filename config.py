import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "20990520")
    API_HASH = environ.get("API_HASH", "714a70d62fc73bf8ec1a5d38adf8f198")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ipsappdevelopers:ipsappdevelopers@cluster0.j5q11.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ipsappdevelopers")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '472034722').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002259804858'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
