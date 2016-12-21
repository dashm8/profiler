import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import os
from collections import Counter
import cookielib


class instegram:
    #ini funcs help
    def GetHTMLCode(url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page
    #init
    def __init__(self,url,project_name,username = "null",password = "null"):
        self.url = url
        self.project_name = project_name
        self.username = username
        self.password = password
        #self.data = GetHTMLCode(self.url)
        if not os.path.isfile(project_name+"/instegram_data"):
            try:
                os.makedirs(project_name+"/instegram_data")
                print "[*] created directory for instegram data"
            except OSError:
                print "[?] directory already exists or faild to create"
    
    #utility functions 
    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""
    def GetProfilePic(self):
        try:
            page = BeautifulSoup(urllib2.urlopen(self.url))
            print "[*] found page"
            profilelink = page.findAll('img')
            link = ""
            for img in profilelink:
                link = img.get("src")
            print "[*] got link from profile"
            file = open(self.project_name + "/instegram_data/profile_pic.jpg",'w+')
            image = urllib.urlopen(link)
            file.write(image.read())
            print "[*] profile image was saved"
            file.close()
        except Exception:
            print "[!] network error no action was made" 
    

    def GetLocation(self,loginrequird):
        #gets the most used location in photos
        try:
            places = []
            if loginrequird:
                page = Login()
            else:
                page = BeautifulSoup(urllib2.urlopen(self.url))
            print "[*] found page"
            allimages = page.findAll('a')
            imagelist = []
            for images in allimages:
                if images.get("class") == "_8mlbc _vbtk2 _t5r8b":
                    imagelist.append(images.get("href"))
        
            for imgs in imagelist:
                imagelink = BeautifulSoup(urllib2.urlopen("www.instagram.com"+ imgs))
                print "[*] found image url www.instagram.com" + imgs
                alllinks = imagelink.findAll('a')
                for images in alllinks:
                    if images.get("class") == "_kul9p _rnlnu":
                        places.append(images.get("title"))

            counterplaces = Counter(places)
            print "most uploaded places" + counterplaces.most_common(3)

        except:
            print "[!] fatal error no internet connection or faild connection"

    def Login(self):
        url = "https://www.instagram.com"
        form_data = {"username":username,"password":password}
        jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        from_data = urllib.urlencode(form_data)
        resp = opener.open(url,form_data)
        return BeautifulSoup(resp)



