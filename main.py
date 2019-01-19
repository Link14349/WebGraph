#!/usr/bin/python
# -*- coding: UTF-8 -*-

from webpage import weight, webpage
import urllib2
import re
import thread
import time
url = raw_input("The url to be crawled: ")
# url = "http://yhzheng.com:30/text/id?id=6"
gotUrls = {}
waitTime = input("End crawling after a few seconds: ")
rcFile = open(".wpgrc")
rc = rcFile.read()
rc = rc.split("\n")
rcs = "Illegal urls: "
for i in rc:
    rcs += i + "; "
print("\033[34m" + rcs + "\033[0m")
def get(pu, url):
    global gotUrls
    global rc
    content = ""
    links = []
    # print(pu)
    # tmp = urlparse.urlparse(url)
    # print("URL1: " + url)
    # url = tmp[0] + "://" + tmp[1]
    # print("URL2: " + url)
    if gotUrls.has_key(url):
        print("\033[36mGot a found url.\033[0m")
        gotUrls[url].links.append(webpage(pu, gotUrls[pu].weight))
        gotUrls[url].weight = weight(gotUrls[url].links)
        # print(gotUrls[url].links)
    else:
        print("Getting " + url + " ......")
        try:
            content = urllib2.urlopen(url).read()
            reg = re.compile('<[^>]*>')
            content = reg.sub(" ", content)
            # print(content)
            links = re.findall(re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"),
                                content)
        except BaseException:
            print("\033[31mHttp error.\033[0m")
            return
        print("\033[32mGot webpage......\033[0m")
        print("\033[33mParsing webpage......\033[0m")
        # print(content)
        gotUrls[url] = webpage(url)
    for i in links:
        flag = False
        for j in rc:
            if j in i:
                flag = True
                break
        if flag:
            print("\033[31mFound a illegal url, stop access.\033[0m")
            continue
        # tmp = urlparse.urlparse(i)
        # print("URL1: " + url)
        # i = tmp[0] + "://" + tmp[1]
        get(url, i)

# get("", url)
thread.start_new_thread(get, ("", url))
for i in range(waitTime, -1, -1):
    print("\033[34mPlease wait " + str(i) + " seconds to show the link graph...\033[0m")
    time.sleep(1)
# for i in gotUrls:
#     gotUrls[i].weight = weight(gotUrls[i].links)
for i in gotUrls:
    print(gotUrls[i].url(), gotUrls[i].weight)
    # print(i)
print("\033[1m\033[32m[FINISH]\033[0m")
rcFile.close()