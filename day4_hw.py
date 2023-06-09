from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def user_kontrol(self): #user bos
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("") 
        passwordInput.send_keys("")
        loginButonu = driver.find_element(By.ID,"login-button")
        loginButonu.click()
        hataMesaji = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testSonuc = hataMesaji.text == "Epic sadface: Username is required"
        print("Hata Mesaji: Epic sadface: Username is required")
        print(f"Test Sonucu: {testSonuc}")
    def password_kontrol(self): #password kontrol
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("a") 
        passwordInput.send_keys("")
        loginButonu = driver.find_element(By.ID,"login-button")
        loginButonu.click()
        hataMesaji = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testSonuc = hataMesaji.text == "Epic sadface: Password is required"
        print("Hata Mesaji: Epic sadface: Password is required")
        print(f"Test Sonucu: {testSonuc}")
    def user_block(self): # user blocked
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user") 
        passwordInput.send_keys("secret_sauce")
        loginButonu = driver.find_element(By.ID,"login-button")
        loginButonu.click()
        hataMesaji = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testSonuc = hataMesaji.text == "Epic sadface: Sorry, this user has been locked out."
        print("Hata Mesaji: Epic sadface: Sorry, this user has been locked out.")
        print(f"Test Sonucu: {testSonuc}")    
    def errorButtonClose(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("") 
        passwordInput.send_keys("")
        loginButonu = driver.find_element(By.ID,"login-button")
        loginButonu.click()
        errorButton = driver.find_element(By.CLASS_NAME,"error-button")
        errorButton.click()
        sleep(5)
        print("Error buton kapatildi")
    def prodoctCounter(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user") 
        passwordInput.send_keys("secret_sauce")
        loginButonu = driver.find_element(By.ID,"login-button")
        loginButonu.click()
        productCounter = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Swag Labs sitesinde su anda {len(productCounter)} adet urun var")
testClass = Test_Sauce()
testClass.user_kontrol()
testClass.password_kontrol()
testClass.user_block()
testClass.errorButtonClose()
testClass.prodoctCounter()
