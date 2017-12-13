import urllib.request
import csv
import time
import re

now = time.strftime('%d-%m-%Y %H:%M:%S')
def getlinks(website):
    links = []
    fp = urllib.request.urlopen(website)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    for line in mystr.split():
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
        if "www" in str(urls):
            links.append(urls)
    links.sort()

    return links

def exportcsv(filename, list):

    with open('filename', 'w', newline='') as newfile:
        a = csv.writer(newfile)
        for x in list:
            a.writerow([x] + [now])

def exporttext(filename, list):

    with open('filename', mode='wt') as myfile:
        for lines in list:
            myfile.write(str(lines) + " " + str(now))
            myfile.write('\n')

def getwebcount(website):
    mywebsite=getlinks(website)
    webcount = 0
    for i in mywebsite:
        webcount += 1
    return webcount