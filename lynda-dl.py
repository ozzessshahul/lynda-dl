# adapted from http://fossbytes.com/how-to-download-lynda-com-videos-using-youtube-dl/

import os
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('https://www.lynda.com/After-Effects-CS5-tutorials/essential-training/59957-2.html') # url from the site you'd like to scrape

for link in BeautifulSoup(response).find_all('a', href=True):
    #print link['href']
    if 'https://www.lynda.com/After-Effects-CS5-tutorials/essential-training/59957-2.html' in link['href']: # parse only the links that contain the key URL to your specific tutorial
        l = link['href']
        #print l
        os.system("youtube-dl --lib-sip:21172023552708@Dclibrary.org yourLogin --password 3357 " + l) # login + password lynda to change. nb : the space after your password is usefull
