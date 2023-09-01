

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'https://py4e-data.dr-chuck.net/comments_1840464.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup('span') # returns a list of spans
sum = 0
for tag in tags:
    span = str(tag) # Convert to string to use in findall 
    print(span)
    num = re.findall("[0-9]+", span) # extract numbers from string
    for y in num:
        y = int(y) # convert to interger to sum total 
        sum = sum + y 
print(sum)        