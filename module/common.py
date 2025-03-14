# 共用函數
import os
import allure
import logging
from module import path

class Common:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, screenshot_name):
        """
        截圖並保存
        - screenshot_name: 截圖名稱
        """
        screenshot_dir = os.path.join(path.SCREENSHOT)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f'{screenshot_name}.png')
        self.driver.get_screenshot_as_file(screenshot_path)  # 截圖餅儲存為圖片
        logging.info(f"截图已保存至: {screenshot_path}")

        # 將截圖添加到 Allure 報告
        with open(screenshot_path, "rb") as screenshot_file:
            allure.attach(screenshot_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
