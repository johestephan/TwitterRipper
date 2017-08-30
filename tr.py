import twitter
import re
import json
import requests
from bs4 import BeautifulSoup

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

outfile = open("Leaktweets.txt","a")

keywords = ["example.com", "Mickey Mouse"]

def hibp_verify(email):
        retstr = ""
        APIendpoints = ["https://haveibeenpwned.com/api/v2/breachedaccount/%s", "https://haveibeenpwned.com/api/v2/pasteaccount/%s"]
        for URL in APIendpoints:
                r = requests.get(URL % email)
                if not r.status_code == 404:
                        data = json.loads(r.text)
                        for item in data:
                                retstr += "%s - %s\n" % (item['Title'], item['IsVerified'])
                        print(retstr)
        return retstr

for item in api.GetListTimeline("MYID"):
        try:
                newD = json.loads(str(item))
                d1 = str(newD["urls"][0]["url"])
                d2 = str(newD["text"])
                d3 = str(newD["id_str"])
                filename = "./%s.txt" % d3
		            print('''%s: %s, %s''' % (d3, d2, d1))
		              if not os.path.exists(filename):
			              outfile.write('''%s: %s, %s\n''' % (d3, d2, d1))
			              #print('''%s: %s, %s\n''' % (d3, d2, d1))
                    r = requests.get(d1)
                    p1 = r.text
                    soup = BeautifulSoup(p1 , "html5lib")
                    pp1 = soup.get_text()	
                    outfile1 = open(filename, "wb")
                    outfile1.write(bytes(pp1, 'UTF-8'))
                    outfile1.close()	
		
                    for word in keywords:
                      if word in pp1.lower():
                        print("FOUND!: %s in %s\n\n" % (word,d3))
                  else:
			              print("%s exists\n\n" % filename)
        except: 
                print(item)
                continue
outfile.close()
