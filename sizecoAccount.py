import requests
import time
from random import getrandbits

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Size? Co account creator")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Inspiried by @mxnnxt")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Created by @donjanwn")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------\n")

session = requests.session()

headers = {
    "Connection": "keep-alive",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"Upgrade-Insecure-Requests": "1",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9"
}


# Input your own information here
prefix = "sizeemailt"
domain = "@gmail.com" # Gmail or use your own catchall domain

password = "Test12345"
firstName = "John"
lastName = "Doe"


billing1 = "123 Wall Street"
billing2 = "Suite 411" ## If no billing2 leave as -> "" 
billingCounty = "New York" # Enter state here spelled out
billingPostcode = "33031" # Enter zip code here
billingTown = "Brooklyn" # Enter city here
phone = "4119114949" # Enter cell here, no dashes or spaces 


times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of account(s) you would like to create: ")))

text_file = open("sizecoAccounts.txt", "w")



def create_account():
	
	print("[" + (time.strftime("%H:%M:%S")) + "]" + " - SUBMITTING INFO.....")
	global session
	global email

	email = (prefix + "{}" + domain).format(getrandbits(40))
	
	
	url = "https://www.size.co.uk/myaccount/register/?"
	payload = {
		"saveDetails"
		"addressPredict":"",
		"billingAddress1":billing1,
		"billingAddress2":billing2,
		"billingCountry":"United States|us", ## US residents should not edit this
		"billingCounty":billingCounty,
		"billingPostcode":billingPostcode, 
		"billingTown":billingTown,
		"confirmPassword":password,
		"email":email,
		"firstName":firstName,
		"lastName":lastName,
		"password":password,
		"phone":phone,
		"saveDetails": "on",
		"shippingAddress1":"",
		"shippingAddress2":"",
		"shippingCountry":"United States|us",
		"shippingCounty":"",
		"shippingPostcode":"",
		"shippingTown":"",
		"useBillingAddress":"on",
		"ev":"SubscribedButtonClick",
		"dl":"https://www.size.co.uk/myaccount/register/?",
		"if":"false",
		"cd[buttonText]":"Register",
		"cd[buttonText]":"Or enter address manually"
	}

	response = session.post(url, data = payload, headers = headers)

	if "Success" in response.text:
		print("[" + (time.strftime("%H:%M:%S")) + "]" +" - SUCCESSFULLY CREATED ACCOUNT "+email+":"+password)
		write()
	else:
		print("[" + (time.strftime("%H:%M:%S")) + "]" +" - ERROR COULD NOT CREATE "+email+":"+password)

def write():

    text_file.write(email + ":" + password + "\n")
	

for i in range (times):
    create_account()
