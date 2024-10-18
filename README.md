# Automated Login Tests using Appium and Selenium

This repository contains automated login tests for the website https://the-internet.herokuapp.com/login. The tests are implemented using Appium, Selenium, and Python's `unittest` framework, and they are intended to run on iOS devices (e.g., iPhone 14) via a Safari browser.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Tests Description](#tests-description)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Example Output](#example-output)

## Prerequisites

Before running the tests, ensure you have the following:

- Python 3.x
- Pip3
- Appium server (globally installed with npm)
- Appium-Python-Client (installed via pip3)
- Selenium WebDriver
- Xcode (for iOS testing on macOS)
- iPhone 14 simulator or a physical device with iOS 18.0

## Tests Description

The tests cover the following scenarios for the login page of the website:

1. **Positive Login Test**: Verifies that valid credentials (`tomsmith` and `SuperSecretPassword!`) successfully log in.
2. **Negative Login Test (Invalid Password)**: Verifies that an invalid password displays the correct error message.
3. **Negative Login Test (Invalid Username)**: Verifies that an invalid username displays the correct error message.

## Setup

Follow these steps to set up your environment for running the tests:

1. **Install npm**: If npm is not installed, you can install it by following instructions [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

   ```bash
   # Install npm if not already installed
   brew install node
   ```

2. **Install Appium Globally**:

   ```bash
   npm install -g appium
   ```

3. **Install Xcode (for iOS and macOS testing)**: Download Xcode from the Mac App Store or use the following command:

   ```bash
   xcode-select --install
   ```
4. **Insstal Xcode command line tools**: Open Xcode and ensure you have the necessary simulators set up (e.g., iPhone 14, iOS 18.0).

5. **Install Python 3.x and necessary packages:** Ensure Python 3 and Pip3 are installed. You can check this by running the following commands:

    ```bash
    python3 --version
    pip3 --version
    ```
    If not installed, you can install Python 3 by following instructions here.

    Then, install the necessary Python packages:
    ```bash
    pip3 install Appium-Python-Client
    pip3 install selenium
    ```

6. **Ensure Appium Server is installed:** After globally installing Appium via npm, ensure the Appium server is ready:

    ```bash
    appium --version
    ```

7. **Prepare iOS simulator or physical device:** Set up an iPhone 14 simulator running iOS 18.0 or connect a physical iPhone device. This can be done through Xcode.


## Running Tests
1. **Start the Appium Server**: Open a terminal and start the Appium server:
    ```bash
    appium
    ```

2. **Open the simulator:** It's recommended to open the simulator first and go to the browser (Safari) and go to [this site](https://the-internet.herokuapp.com/login).

3. **Run the Python Test:**
After starting the Appium server and the simulator, run the tests using Python 3:
    ```bash
    python3 test_login.py
    ```
    This will execute the login tests defined in the `test_login.py` script. The results of the test will be displayed in the terminal, indicating whether the tests passed or failed.

## Example Output
When running the tests, you should see something similar to this in your terminal:

```csharp
Positive Test Passed: You logged into a secure area!
Negative Test with Invalid Password Passed: Your password is invalid!
Negative Test with Invalid Username Passed: Your username is invalid!
----------------------------------------------------------------------
Ran 3 tests in 35.678s

OK
```