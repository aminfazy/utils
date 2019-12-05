import re
from mechanize import Browser
import pdb
from bs4 import BeautifulSoup as bs
br = Browser()
br.open("http://172.16.26.43/attendanceinfo/")
br.select_form(name="search")
br["name"] = "1821cs01"
br["month"] = ['11']
response = br.submit()
# print(response.get_data())
# print(response.geturl())
t = response.get_data()

print("here")

soup = bs(t, "html.parser")

# print(a[0:3].text)
# print(a)
# print(soup.findAll("td")[-1].text)
# print(soup.findAll("td")[0:3][-1].text)
length = len(soup.findAll("td"))

a = soup.findAll("td")
# print(a)

if length < 1:
	print("Data not available for this duration, Check the data in script")
	exit(0)
roll = [a[i] for i in range(0,length,3)]
name = [a[i] for i in range(1,length,3)]
attend = [a[i] for i in range(2,length,3)]
# for i in range(length):
	# print(a[i].text, "--->",a[i].text,"--->",a[i][2].text)
# pdb.set_trace()
for i in range(len(attend)):
	print(roll[i].text, name[i].text, attend[i].text)

