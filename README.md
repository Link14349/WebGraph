# WebGraph
This is a crawler similar to Google crawling webpages.

## Algorithm principle
The specific principle of this algorithm is to give an initial web page, then access all the hyperlinks, and then click on the hyperlinks to access the hyperlinks in the web pages it points to, and so on. And based on the number of times the page is linked and the weight of the linked page, the weight of the page is calculated.

## Webpage class
This is a class that stores web page information.
Module: webpage
### Usage
``` python
wp = webpage(url, [weight = 0.001, links = []])
```
#### Create a new object:
``` python
from webpage import webpage
url = "https://www.google.com/"
wp = webpage(url)
```
#### Member function
- url()
TODO: For get the url of this webpage
demo:
``` python
from webpage import webpage
url = "https://www.google.com/"
wp = webpage(url)
print(wp.url()) # https://www.google.com/
```

## weight(links) function
This is a function that can calculate the connected web page based on the linked web page.
Module: webpage
### Usage
``` python
from webpage import webpage, weight
wp1 = webpage("https://www.google.com/")
wp2 = webpage("http://nodejs.org/")
wp3 = webpage("http://www.github.com/")
wp1.links.append(wp2)
wp1.links.append(wp3)
print(weight(wp1.links)) # 0.002
```

## get(pu, url) function
This is a function that can give an initial page and then crawl information continuously.
Global
### Usage
``` python
from webpage import weight, webpage
import urllib2
import re
rcFile = open(".wpgrc")
rc = rcFile.read()
rc = rc.split("\n")
url = "http://yhzheng.com"
get("", url)
rcFile.close()
```

## License
MIT