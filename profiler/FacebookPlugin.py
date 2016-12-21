import urllib
import urllib2
import os
import BeautifulSoup
import requests


class facebook:
    """
    this is a class for facebook  oprations in profiler workspace feel free to use this class for whatever you would like 
    use the login fucktion when you need to accses non public data (the function is used autumaticly when you must use is)

    """
    def __init__(self,usernameV,project_name,username = "none",password = "none"):
        self.username  = username
        self.password = password
        self.url = "www.facebook.com/" + usernameV
        self.usernameV = usernameV
        self.project_name = project_name
        if not os.path.isfile(project_name+"/facebook_data"):
            try:
                os.makedirs(project_name+"/facebook_data")
                print "[*] created directory for facebook data"
            except OSError:
                print "[?] directory already exists or faild to create"


    def GetProfilePic():
        try:
            page = BeautifulSoup(urllib2.urlopen(self.url))
            print "[*] found page"
            profilelink = page.get('img')
            link = ""
            for images in profilelink:
                if images.get('class') == "profilePic img":
                    link = images.get('class')
                    break
            image = urllib.urlopen(link)
            file = open(self.project_name + "/facebook_data/ProfilePic.jpg",'w')
            file.write(image.read())
        except Exception:
            print "[!] connection error"


    def Login(self):
        url = "https://www.facebook.com/"
        form_data = {"email":self.username,"pass":self.password}
        jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        from_data = urllib.urlencode(form_data)
        resp = opener.open(url,form_data)
        return BeautifulSoup(resp)

    def GetFriendList(self):
        headers = {'user-agent': '/v2.8/"+ self.usernameV +"/friendlists HTTP/1.1"'}
        r = requests.get("graph.facebook.com",headers=headers)
        print r