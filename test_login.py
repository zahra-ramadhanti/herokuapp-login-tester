from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from appium.webdriver.webdriver import AppiumOptions

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = AppiumOptions()
        self.desired_caps.set_capability('platformName', 'iOS')
        self.desired_caps.set_capability('platformVersion', '18.0')
        self.desired_caps.set_capability('deviceName', 'iPhone 14')
        self.desired_caps.set_capability('browserName', 'Safari')
        self.desired_caps.set_capability('automationName', 'XCUITest')
        self.desired_caps.set_capability('noReset', True)
        self.desired_caps.set_capability('safariOptions', {'technologyPreview': True})
        self.desired_caps.set_capability('webviewConnectTimeout', 60000)

        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=self.desired_caps)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, value)))

    def test_positive_login(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        self.wait_for_element(By.ID, 'username')

        username = self.wait_for_element(By.ID, 'username')
        password = self.wait_for_element(By.ID, 'password')

        username.send_keys('tomsmith')
        password.send_keys('SuperSecretPassword!')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        self.wait_for_element(By.CSS_SELECTOR, '.flash.success')
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("You logged into a secure area!", flash_message)
        print(f"Positive Test Passed: {flash_message}")

    def test_negative_login_invalid_password(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        self.wait_for_element(By.ID, 'username')

        username = self.wait_for_element(By.ID, 'username')
        password = self.wait_for_element(By.ID, 'password')

        username.send_keys('tomsmith')
        password.send_keys('invalidpassword')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        self.wait_for_element(By.CSS_SELECTOR, '.flash.error')
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("Your password is invalid!", flash_message)
        print(f"Negative Test with Invalid Password Passed: {flash_message}")

    def test_negative_login_invalid_username(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

        self.wait_for_element(By.ID, 'username')

        username = self.wait_for_element(By.ID, 'username')
        password = self.wait_for_element(By.ID, 'password')

        username.send_keys('invalidusername')
        password.send_keys('SuperSecretPassword!')

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        self.wait_for_element(By.CSS_SELECTOR, '.flash.error')
        
        flash_message = self.driver.find_element(By.CLASS_NAME, 'flash').text
        self.assertIn("Your username is invalid!", flash_message)
        print(f"Negative Test with Invalid Username Passed: {flash_message}")


if __name__ == '__main__':
    unittest.main()