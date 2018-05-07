#Automatic Birthday wisher on facebook background version i.e
# not showing window and gui to user.
#One time set up, Paste it into Startup folder.
import re
from fbchat import Client
from fbchat.models import *
import datetime
from getpass import getpass

now= datetime.datetime.now()
k=now.strftime("%d-%m")
file = open("Database.txt", 'r')
cont = file.read()
username=input("Username:")


if k in cont:
    
    patt1=r"([\w]+) ([\w]+):"+k
    mat=re.findall(patt1,cont)
    for _,ele in enumerate(mat):
        name=ele[0]+" "+ele[1]    
        client = Client(username, getpass())
        users = client.searchForUsers(name)
        user = users[0]    
        client.sendLocalImage("cake.jpg", 'Happy Birthday' + name, thread_id=user.uid, thread_type=ThreadType.USER)
    
else:
    print("NO friends have Birthday today.")





