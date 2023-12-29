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
from chromedriver_py import binary_path
import os

class TestCopologinlogout():
  SERVER_TIMEOUT = 10
 
  @classmethod 
  def setup_class(cls):
    options = webdriver.ChromeOptions()
    options.enable_downloads = True
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--enable-file-cookies")
    cls.driver = webdriver.Remote(command_executor="http://copo_browser:3000/webdriver", options=options)
    cls.driver.implicitly_wait(5) 
    #cls.driver.delete_all_cookies()
    cls.vars = {}
 
  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
  
  def test_login(self):
    self.driver.get("http://copo-new.cyverseuk.org:8000/copo")
    self.wait_for_page()
    #self.driver.set_window_size(1188, 839)
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "onetrust-reject-all-handler")))
    self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys(os.environ['COPO_WEB_USER_PW'])
    self.driver.find_element(By.ID, "username").send_keys(os.environ['COPO_WEB_USER'])
    self.driver.find_element(By.CSS_SELECTOR, "#signin-button > .mat-button-wrapper").click()
    time.sleep(10)
    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "acceptCookies")))
    self.driver.find_element(By.ID, "acceptCookies").click()
    time.sleep(5)
    elements = self.driver.find_elements(By.XPATH, "//span[contains(.,\'Work Profiles\')]")
    assert len(elements) > 0
  
  def test_logout(self):
    self.driver.get("http://copo-new.cyverseuk.org:8000/copo/")
    self.wait_for_page()
    self.driver.set_window_size(1188, 839)
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".caret").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Logout\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.get("https://orcid.org/signout")
  
  def wait_for_page(self):
    WebDriverWait(self.driver, self.SERVER_TIMEOUT).until(
        lambda wd: self.driver.execute_script("return document.readyState") == 'complete',
        "Page taking too long to load"
    ) 
