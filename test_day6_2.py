# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from contants import globalContants
from selenium.webdriver.support import expected_conditions as ec

class TestDay6_2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    # self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def waitForElementVisibile(self,locator,timeout=5): # bu fonksiyon yukarida kod tekrarini engellemek icin tanimlandi
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))


  def test_day6_2(self):
    self.driver.get(globalContants.URL)
    self.driver.maximize_window()
    self.waitForElementVisibile((By.ID,"user-name"))
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    userInput = self.driver.find_element(By.ID, "user-name")
    userInput.send_keys("standard_user")
    self.waitForElementVisibile((By.ID,"password"))
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    passInput = self.driver.find_element(By.ID, "password")
    passInput.send_keys("secret_sauce")
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket")))
    itemSelect = self.driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > .inventory_item_name")
    itemSelect.click()
    self.waitForElementVisibile((By.CSS_SELECTOR,".shopping_cart_link"))
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link")))
    itemAdd = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    itemAdd.click()
    basketIcon = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    basketIcon.click()
    removeItem = self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
    removeItem.click()
    self.waitForElementVisibile((By.ID,"react-burger-menu-btn"))
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    burgerMenu = self.driver.find_element(By.ID, "react-burger-menu-btn")
    burgerMenu.click()
    self.waitForElementVisibile((By.ID,"logout_sidebar_link"))
    # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    logoutButton = self.driver.find_element(By.ID, "logout_sidebar_link")
    logoutButton.click()
    self.driver.close()
