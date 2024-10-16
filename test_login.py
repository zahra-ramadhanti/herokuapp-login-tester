from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '18.0',
            'deviceName': 'iPhone 16',
            'browserName': 'Safari',
            'automationName': 'XCUITest',
            'noReset': True,
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def test_positive_login(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))

        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')

        username.send_keys('tomsmith')
        password.send_keys('SuperSecretPassword!')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash success')))
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("You logged into a secure area!", flash_message)
        print(f"Positive Test Passed: {flash_message}")

    def test_negative_login_invalid_password(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))

        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')

        username.send_keys('tomsmith')
        password.send_keys('wrongpassword!')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash error')))
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("Your password is invalid!", flash_message)
        print(f"Negative Test Passed: {flash_message}")

    def test_negative_login_invalid_username(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))

        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')

        username.send_keys('invaliduser')
        password.send_keys('SuperSecretPassword!')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash error')))
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("Your username is invalid!", flash_message)
        print(f"Negative Test Passed: {flash_message}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
