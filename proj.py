from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select #used for dropdown
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

fir_serv = Service("./webdriver/chromedriver.exe")
fir_driver = webdriver.Chrome(service = fir_serv)
wait = WebDriverWait(fir_driver, 10)
fir_driver.get('https://tutorialsninja.com/demo/')
time.sleep(2)
fir_driver.maximize_window()
time.sleep(2)

# Phones and PDAs
ph_cl = fir_driver.find_element(By.XPATH, "//html/body/div[1]/nav/div[2]/ul/li[6]/a")
ph_cl.click()
time.sleep(2)

# Palm Three Treo
ph = fir_driver.find_element(By.XPATH, "//a[text()='Palm Treo Pro']")
ph.click()
# fir_driver.save_screenshot('iphone.png')
time.sleep(2)

# viewing the pic
img = fir_driver.find_element(By.XPATH, "//ul[@class='thumbnails']/li[1]/a")
img.click()
time.sleep(2)

# viewing the next pic
nxt_img = fir_driver.find_element(By.CSS_SELECTOR, "button[class='mfp-arrow mfp-arrow-right mfp-prevent-close']")
# clicking next for 5 times
for i in range(0,3):
    nxt_img.click()
    time.sleep(2)

# saving screenshot with any random number from 0-100
# fir_driver.save_screenshot('screenshot#'+ str(random.randint(0,101)) +'.png')

# close the image viewer
cl_img = fir_driver.find_element(By.CSS_SELECTOR, "button[class= 'mfp-close']")
cl_img.click()
time.sleep(2)

# Quantity searchbox
qua = fir_driver.find_element(By.XPATH, "//div/input[@id='input-quantity']")
qua.click()
time.sleep(2)

# There's 1 in the quantity searchbox
qua.clear()
time.sleep(2)
qua.send_keys(2)

# Add to Cart
cart = fir_driver.find_element(By.XPATH, "//button[@id ='button-cart']")
cart.click()
time.sleep(2)

#select phones done and added to cart, next is to select a a laptop

# Laptop (Dropdown lookalike)
lap = fir_driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']/li[2]/a")
action = ActionChains(fir_driver) #the laptop has a dropdown, we need to select another item in the dropdown
action.move_to_element(lap).perform()
time.sleep(2)
show_all = fir_driver.find_element(By.XPATH, "//a[text()='Show AllLaptops & Notebooks']") #it drops down and pick this
show_all.click()
time.sleep(2)

# pick an hp laptop
hp = fir_driver.find_element(By.XPATH, "//a[text()='HP LP3065']")
hp.click()
time.sleep(2)


# scrolling down the page
add_to_cart = fir_driver.find_element(By.XPATH, "//button[@id='button-cart']")
time.sleep(2)
add_to_cart.location_once_scrolled_into_view  #the page will scroll down to have a good view of "Add to cart"
time.sleep(2)

# Getting the calendar button and choosing a delivery date
calen = fir_driver.find_element(By.CSS_SELECTOR, "i[class='fa fa-calendar']")
calen.click()
time.sleep(2)

# selecting the delivery day(the random date picked must be lower than the delivery date we want)
rand_date = fir_driver.find_element(By.XPATH, "//th[@class='picker-switch']") #working with a random date/month
next_cal = fir_driver.find_element(By.CSS_SELECTOR, "th[class='next']") #this is the next on the calendar

# selecting the date
while rand_date.text != 'August 2023':          #the random date is not equal to the delivery date we want
    next_cal.click()
time.sleep(3)

# picking a specific date(August 1, 2023)
deli_date = fir_driver.find_element(By.XPATH, "//div[@class='datepicker']/div/table/tbody/tr/td[2]")
deli_date.click()
time.sleep(2)

#Add to Cart
# we dont need to change the 1 in the laptop quantitybox
cart = fir_driver.find_element(By.XPATH, "//button[@id ='button-cart']")
cart.click()
time.sleep(2)

# Checking the cart total
cart_to = fir_driver.find_element(By.ID, "cart-total")
cart_to.click()
time.sleep(2)

# Checkout
check_out = fir_driver.find_element(By.XPATH, "//p[@class='text-right']/a[2]")
check_out.click()
time.sleep(2)

#  Checkout as a Guest(radio)
gue = fir_driver.find_element(By.XPATH, "//div[@class='col-sm-6']/div[2]/label/input[@type='radio']")
gue.click()
time.sleep(2)

# Continue button (Continue to Step 2- Billing)
cont = fir_driver.find_element(By.XPATH, "//div[@class='col-sm-6']/input[@value='Continue']")
cont.click()
time.sleep(2)

# # Continue to Step 2: Billing Details
first_name = fir_driver.find_element(By.XPATH, "//fieldset[@id='account']/div[2]/input")
time.sleep(1)
first_name.click()
first_name.send_keys('Shadea')
time.sleep(1)
first_name.send_keys(Keys.BACKSPACE)
time.sleep(1)

company = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[1]/input")
time.sleep(1)
company.click()
company.send_keys('ShadeKhiat')
time.sleep(1)

last_name = fir_driver.find_element(By.XPATH, "//fieldset[@id='account']/div[3]/input")
time.sleep(1)
last_name.click()
last_name.send_keys('Ayodele')
time.sleep(1)

addr = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[2]/input")
time.sleep(1)
addr.click()
addr.send_keys('Bolton Road, Kearsley')
time.sleep(1)

email = fir_driver.find_element(By.XPATH, "//fieldset[@id='account']/div[4]/input")
time.sleep(1)
email.click()
email.send_keys('bayodele73@gmail.com')
time.sleep(1)

pho = fir_driver.find_element(By.XPATH, "//fieldset[@id='account']/div[5]/input")
time.sleep(1)
pho.click()
pho.send_keys('07424543579')
time.sleep(1)

city = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[4]/input")
time.sleep(1)
city.click()
city.send_keys('Bolton')
time.sleep(1)

post = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[5]/input")
time.sleep(1)
post.click()
post.send_keys('BL8HJ')
time.sleep(1)

country = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[6]/select")
dropdown = Select(country)
time.sleep(2)
dropdown.select_by_index(164) #Nigeria is index of 164
time.sleep(2)

region = fir_driver.find_element(By.XPATH, "//fieldset[@id='address']/div[7]/select")
downdrop = Select(region)
time.sleep(1)
downdrop.select_by_visible_text('Lagos')
time.sleep(2)

# Step 3 is skipped because we skipped it in Step 2
# Continue to Step 4
# scroll down to get a better view of the webpage
conti4 = fir_driver.find_element(By.CSS_SELECTOR, "div[class='pull-right']")
time.sleep(1)
conti4.location_once_scrolled_into_view
conti4.click()
time.sleep(5)

# Continue  to Step 5
nxt = fir_driver.find_element(By.XPATH, "//*[@id='button-shipping-method']")
time.sleep(2)
nxt.click()
time.sleep(5)

# Step 5
# click the terms and agreement
tnc = fir_driver.find_element(By.XPATH, "//input[@name='agree']")
time.sleep(2)
tnc.click()
time.sleep(3)

# Continue  to Step 6
nx6t = fir_driver.find_element(By.XPATH, "//input[@id='button-payment-method']")
time.sleep(2)
nx6t.click()
time.sleep(5)

# Confirm Order
amt = fir_driver.find_element(By.XPATH, "//div[@class='table-responsive']/table/tfoot/tr[3]/td[2]")
print('Total amount: ' + amt.text)
con_order = fir_driver.find_element(By.XPATH, "//input[@id='button-confirm']")
time.sleep(2)
con_order.click()
time.sleep(2)

# Confirmation Slip
cosl = fir_driver.find_element(By.XPATH, "//div[@id='content']/h1")
time.sleep(1)
print('Receipt: ' + cosl.text)


input('Press Enter to stop......')




# this is for pop-ups
# child_window = fir_driver.window_handles[1]
# fir_driver.switch_to.window(child_window)

