from InstegramPlugin import instegram
from FacebookPlugin import facebook
import os
import requests


#usage funcs
def StartUp(project_name):
    if not os.path.isfile(project_name):
        try:
            os.makedirs(project_name)
            print "[*] directory " + project_name + " was created"
        except OSError:
            print "[?] directory already exists or faild to create"
def instagramfunc(username,login,username1="null",password="null"):
    a = instegram("https://www.instagram.com/" + username +"/?hl=en",projectname,username1,password)
    a.GetProfilePic()
    a.GetLocation(login)
def UploadFolder():
    onlyfiles = [f for f in os.listdir(projectname) if os.path.isfile(os.path.join(projectname, f))]
    for files in onlyfiles:
        r = requests.post(("127.0.0.1",8080),files)
#def RequstData():

def facebookfunc(url,username1="none",password1="none"):
    facebook1 = facebook(url,projectname,username1,password1)
    facebook1.GetFriendList()



print ""
print "[*] hello and welcome to profiler desktop tool "
print ""
print ""
print "choose project name: "
projectname = raw_input()
StartUp(projectname)
print "choose plugins you can choose as many options as you want: "
print ""
print ""
print ""
print "1:instegram"
print "2:Facebook"
print "3:twitter"
print "4:google dork"
print "5:simple web crewler"
print ""
print ""


iniput = raw_input()
if '1' in iniput:
    username = raw_input("enter the username of your victim")
    login = raw_input("enter 0 or 1 for true or false to log in with your account")
    if login == 1:
        login = True
    else:
        login = False
    if login:
        username1 = raw_input("username")
        password = raw_input("password")
        instagramfunc(username,login,username1,password)
    else:
        instagramfunc(username,login)
if '2' in iniput:
    url = raw_input("enter victim username")
    facebookfunc(url)
        
#UploadFolder()

