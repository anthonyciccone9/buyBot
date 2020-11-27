# Author: github/anthonyciccone9
# Basic bot to buy something on best buy.
# python3 -m pip install selenium
# THIS IS NOT COMPLETE but its pretty close
# the chromedriver and geckodriver included might be out of date

# if you wanted to use this for another buy site you can inspect element and find all the correct classes / xpaths for each element.
# fill in the args in the main method

from selenium import webdriver
import time

def buy(args):
	# driver = webdriver.Chrome('./chromedriver') # can be used if using chromedriver
	driver = webdriver.Firefox(executable_path='./geckodriver') # can be used if using geckodriver
	print("started up")
	driver.get(args["product_url"])
	print("Opening " + args["product_url"])
	time.sleep(1)
	driver.find_element_by_class_name("add-to-cart-button").click()
	print("added to cart")
	time.sleep(1)
	driver.find_element_by_class_name("cart-link").click()
	print("viewing cart")
	time.sleep(3)
	driver.find_element_by_class_name("checkout-buttons__checkout").click()
	print("checking out")
	time.sleep(6)
	driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[4]/div/div[2]/button').click()
	print("who are you?")
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.firstName"]').send_keys(args["first_name"])

if __name__ == '__main__':
	# Fill in the information below before running
	args = {
		"product_url": "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324", # buy page, include http https etc
		"first_name": "Anthony",
		"last_name": "Ciccone", 
		"email": "email", 
		"address": "address", # Street Address
		"zip": "zip", # zip code
		"phone_number": "phonenumber",
		"card_number": "cardnumber", 
		"cvv": "cvv"
	} 
	buy(args) #runs the buy method
