import urllib2
from bs4 import BeautifulSoup
import sys
import time



def getGoogleCount(query):
    headers = {'User-agent':'Mozilla/11.0'}
    url = 'http://www.google.com/search?q='+urllib2.quote(query)
    req = urllib2.Request(url,None,headers)
    site = urllib2.urlopen(req)
    soup = BeautifulSoup(site)
    s = str(soup.find("div",{"id":"resultStats"}))
    count = float(s.split('>')[1].split('<')[0].split(' ')[1].replace(",",""))
    return count

if __name__ == '__main__':
    ip = raw_input('Enter the query : ')
    count = getGoogleCount(ip)
    print "Number of Results for ",ip," = ",count 



