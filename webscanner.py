import urllib.request
import csv
import time
import re


def getlinks(website):
    now = time.strftime('%d-%m-%Y %H:%M:%S')
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

    with open('tmp.csv', 'w', newline='') as qp:
        a = csv.writer(qp, delimiter=',')
        a.writerows(links)

    with open('tmp.txt', mode='wt') as myfile:
        for lines in links:
            myfile.write(str(lines) + " " + str(now))
            myfile.write('\n')
    print(links)
getlinks("https://www.reddit.com/r/2007scape/")