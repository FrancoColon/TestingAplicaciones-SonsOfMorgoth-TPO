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

class TestCase1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_case1(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("sample")
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.CSS_SELECTOR, "form > p:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(2) td:nth-child(5) #itemImage").click()
    self.driver.find_element(By.LINK_TEXT, "Add to Cart").click()
    cart1 = self.driver.find_element(By.CLASS_NAME, "link").text
    assert "CART 1" in cart1
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(3) td:nth-child(4) #itemImage").click()
    self.driver.find_element(By.LINK_TEXT, "Add to Cart").click()
    cart2 = self.driver.find_element(By.CLASS_NAME, "link").text
    assert "CART 2" in cart2
    self.driver.find_element(By.ID, "cartIcon").click()
    self.driver.find_element(By.LINK_TEXT, "Remove").click()
    assert "CART 1" in cart1
    self.driver.find_element(By.ID, "cartIcon").click()
    self.driver.find_element(By.LINK_TEXT, "Remove").click()
    cart0 = self.driver.find_element(By.CLASS_NAME, "link").text
    assert "CART 0" in cart0
