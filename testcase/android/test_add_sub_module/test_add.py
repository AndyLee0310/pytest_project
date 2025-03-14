import allure, re
from appium.webdriver.webdriver import By

@allure.feature('加法測試')
@allure.feature('v1.0')
class TestAdd():

    @allure.story('加法測試')
    @allure.title('加法測試')
    def test_case01(self, open_app, close_app):

        with allure.step('輸入數字並加法運算'):
            driver = open_app
        with allure.step('輸入數字並加法運算'):
            driver.find_element(By.ID,'com.google.android.calculator:id/digit_9').click()
            driver.find_element(By.ID, 'com.google.android.calculator:id/op_add').click()
            driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8').click()
            driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()
            actual_result = driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
        with allure.step('驗證結果'):
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '17'
