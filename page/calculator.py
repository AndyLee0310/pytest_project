import os
import allure
import logging
from module import path
from appium.webdriver.webdriver import By, WebDriver

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def number_1_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_1')

    @property
    def number_2_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_2')

    @property
    def number_3_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_3')

    @property
    def number_4_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4')

    @property
    def number_5_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_5')

    @property
    def number_6_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_6')

    @property
    def number_7_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_7')

    @property
    def number_8_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8')

    @property
    def number_9_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_9')

    @property
    def number_0_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_0')
    
    @property
    def add_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/op_add')

    @property
    def sub_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/op_sub')

    @property
    def mul_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/op_mul')
    
    @property
    def div_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/op_div')

    @property
    def equal_button(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/eq')

    @property
    def result_field(self):
        return self.driver.find_element(By.ID, 'com.google.android.calculator:id/result_final')

    # def take_screenshot(self, screenshot_name):
    #     # 保存截图到当前目录下的 screenshots 文件夹
    #     screenshot_dir = os.path.join(path.SCREENSHOT)
    #     if not os.path.exists(screenshot_dir):
    #         os.makedirs(screenshot_dir)

    #     screenshot_path = os.path.join(screenshot_dir, f'{screenshot_name}.png')
    #     self.driver.get_screenshot_as_file(screenshot_path)  # 截图并保存为文件
    #     logging.info(f"截图已保存至: {screenshot_path}")

    #     # 将截图附加到 Allure 报告中
    #     with open(screenshot_path, "rb") as screenshot_file:
    #         allure.attach(screenshot_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
