import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestLogins(unittest.TestCase):

    def setUp(self):
        # Inicializa o Chrome (precisa do chromedriver no PATH)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Fecha o navegador após cada teste
        self.driver.quit()

    def test_CT001_saucedemo_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)
        self.assertIn("inventory", driver.current_url)

    def test_CT002_herokuapp_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        time.sleep(2)
        self.assertIn("/secure", driver.current_url)
        self.assertIn("You logged into a secure area!", driver.page_source)

    def test_CT003_practice_login(self):
        driver = self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")

        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        time.sleep(2)
        self.assertIn("practicetestautomation.com/logged-in-successfully", driver.current_url)
        self.assertIn("successfully logged in", driver.page_source.lower())

    def test_CT004_orangehrm_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(3)
        self.assertIn("/dashboard/index", driver.current_url)

if __name__ == "__main__":
    unittest.main()
