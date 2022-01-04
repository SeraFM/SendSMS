from time import sleep
from selenium import webdriver
from keyboard import press


driver = webdriver.Chrome('chromedriver')
driver.minimize_window()


def sendSMS():
    driver.get("https://globfone.com/send-text/")
    sleep(0.5)
    textbox = driver.find_element_by_xpath('/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div[2]/form/input')
    textbox.click()
    textbox.send_keys("UPDATE")
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div[2]/a")
    nextbutton.click()
    sleep(4)
    country = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]")
    country.click()
    country.send_keys("COUNTRY") # <- COUNTRY NAME HERE (For example: "Greece")
    press('enter')
    sleep(1)
    pnum = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input")
    pnum.click()
    pnum.send_keys("PHONE NUM") # <- PHONE NUMBER HERE
    sleep(0.5)
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]")
    nextbutton.click()
    sleep(2)
    input_text = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/textarea")
    input_text.click()
    sleep(1)
    input_text.send_keys("SMS HERE") # <- SMS TEXT HERE
    sleep(1)
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]")
    nextbutton.click()
    sleep(20)
    print("SMS sent!")

sendSMS()
