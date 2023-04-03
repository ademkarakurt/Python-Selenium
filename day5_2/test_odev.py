from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path # dosya islemleri yapan eklenti
from datetime import date



class Test_DemoClass:
    #her testten once cagrilir 
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #gunun tarihini al 
        #self.bugun = str(date.today()) 
        #gunun tarihini alip o tarihe gore yoksa dosya adi olusturulacak
        self.dosyaYolu = str(date.today())
        Path(self.dosyaYolu).mkdir(exist_ok=True) # exist_ok= True ise dosya varsa olusturma 

    # her testten sonra cagrilir
    def teardown_method(self):
        self.driver.quit() # siteyi kapatir

    def waitForElementVisibile(self,locator,timeout=5): # bu fonksiyon yukarida kod tekrarini engellemek icin tanimlandi
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))

     
    @pytest.mark.skip() # skip ile pytest'te alttaki fonksiyonu atla dedik
    def atlanan_func(self,username):
        self.waitForElementVisibile(By.ID,"user-name")
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("")
        loginButonu = self.driver.find_element(By.ID,"login-button")
        loginButonu.click()


    @pytest.mark.parametrize("username,password",[("","")])
    def test_nousernameandpassword(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")

        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Username is required"

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-nousernameandpassword-.png")

    
    # Sadece sifre alani bos gecildiğinde uyari mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    @pytest.mark.parametrize("username,password",[("standard_user","")])
    def test_nopassword(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Password is required"

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-nopassword-.png")


    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_lockedoutuser(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")

        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-lockedoutuser-.png")


# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. 
# Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    @pytest.mark.parametrize("username,password",[("","")])
    def test_iconX(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        iconredX1=self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1)")
        sleep(2)
        iconredX2=self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2)")
        sleep(2)
        
        closeBtn=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        closeBtn.click()

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-iconX-.png")


    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_std_user(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-std_user-.png")

    
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
    def test_numberofproduct(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
       
        listofproduct=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(listofproduct)==6

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-numberofproduct-.png")


    #Sepete ürün eklenmelidir.
    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_addproduct(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        addProduct=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
        addProduct.click()

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-addProduct-.png")

    # Sepetteki ürün silinmelidir.
    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_delproduct(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        addProduct1=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button")
        addProduct1.click()

        addProduct2=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button")
        addProduct2.click()

        goShopping=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
        goShopping.click()

        delproduct1=self.driver.find_element(By.ID,"remove-sauce-labs-onesie")
        delproduct1.click()

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-delProduct-.png")

    

    # Başarılı giriş işleminden sonra çıkış yapmılmalıdır.
    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_logout(self,username,password):
        self.waitForElementVisibile((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisibile((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        action=ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        menuBtn=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        menuBtn.click()

        self.driver.implicitly_wait(5)

        logoutBtn=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
        logoutBtn.click()

        self.driver.save_screenshot(f"{self.dosyaYolu}/test-logout-.png")
  
    
