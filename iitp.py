import re
import xmltodict
from mechanize import Browser
import pdb
from bs4 import BeautifulSoup as bs
import argparse


parser = argparse.ArgumentParser(description="auto login")
parser.add_argument('-alt', type = int,  default = 0, help = 'Enter 1 to use alternate login')

br = Browser()
br.set_handle_robots(False) # this is important as some sites disallow scraping
br.open("http://10.120.120.22:8090/httpclient.html")
#br.forms()[0].name #this is how to find names of forms in a webpage
# this is how to get attributes of the form to be used to supply values
#for control in br.form.controls:
#       print(control)
#	print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

opt = parser.parse_args()

br.select_form(name="frmHTTPClientLogin")
if opt.alt == 1:
	br["username"] = "guest"
	br["password"] = "Biht@123"
else:

	br["username"] = "fazail_1821cs01"
	br["password"] = '9_16_1988'
response = br.submit()
t = response.get_data() # if t is in form of xml of byte data then it needs to be paresed 
data = xmltodict.parse(t)

a = data['requestresponse']['status']
b= data['requestresponse']['message']

print(a)
print(b)
