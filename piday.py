import requests
import re 

n = 223232
r = requests.get('http://subidiom.com/pi/piday.asp',params={'s':n})

html_doc = r.text


print(float(re.findall(pattern="Search time was (.*?) second",string=html_doc)[0]))

print(re.findall(pattern="appears at the ([0-9,]*?)(st|nd|rd|th| )",string=html_doc)[0][0])

print(re.findall(pattern="<font size=4>(\d*?)<font color=0f00ff>",string=html_doc)[0])
print(re.findall(pattern="</font>(\d*?)<br>",string=html_doc)[0])