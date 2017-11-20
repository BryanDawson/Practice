"""
Simple Web Page Decoder practice program.


Solution for:
http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Note: pretty simple script.  Most of the effort here was digging into the
      BeautifulSoup documentation and figuring out the fields etc...
      (just scratched the surface of web scraping)

"""

import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup

testurl = "https://www.nytimes.com/"

r_html = requests.get(testurl).text


soup = BeautifulSoup(r_html, "html.parser")


for headline in soup.find_all(class_="story-heading"):
    if headline.a:
        print(headline.a.text.strip())
    else:
        print(headline.contents[0].strip())





