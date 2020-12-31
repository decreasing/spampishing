from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from halo import Halo
import random
import string
import time
import os
import signal
import sys

def signal_handler(signal, frame):
    print(RED + '\n\nExiting...\n\n' + END)
    driver.close()
    sys.exit(0)

GREEN = '\33[32m'
RED = '\33[31m'
END = '\33[0m'

def random_string(stringLength=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))

def random_email():
    domains = ["@yahoo.com","@hotmail.com","@gmail.com","@aol.com","@mail.com"]
    return random_string(5) + random.choice(domains)

url = "PUT URL HERE"
#url = "https://api.ipify.org"
amount = 0

os.system('clear')
while True:
    try:

        email = random_email()
        password = random_string()
        amount = amount + 1

        spinner = Halo(text="[SUBMIT: " + str(amount) + "]" + " Submitting email " + GREEN + email + END + " with passowrd " + GREEN + password + END + " at " + GREEN + time.ctime() + END, spinner="dots")
        spinner.start()

        options = Options()
        options.headless=True

        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy_type', 1)
        profile.set_preference('network.proxy.http', "127.0.0.1")
        profile.set_preference('network.proxy.port', 9050)

        driver = webdriver.Firefox(firefox_profile=profile, options=options)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        try:
            driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[2]/h1/form/label[3]/button').click()
            spinner.succeed()
            spinner.stop()
        except:
            spinner.fail()
            spinner.stop()
        driver.close()
    except KeyboardInterrupt:
        print(RED + '\n\nExiting...\n\n' + END)
        driver.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
