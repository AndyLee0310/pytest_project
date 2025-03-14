import allure
import pytest
import re
import logging
from module.common import Common
from page.calculator import CalculatorPage

@allure.feature('加法測試')
@allure.feature('v1.0')
class TestAdd():

    @allure.story('加法測試')
    @allure.title('[case01]加法測試')
    @pytest.mark.add_sub_basic
    def test_add_case01(self, open_app, close_app):
        driver = open_app
        common = Common(driver)
        calculator_page = CalculatorPage(driver)

        with allure.step('點擊數字8'):
            calculator_page.number_8_button.click()
            common.take_screenshot('點擊數字8')

        with allure.step('點擊加號'):
            calculator_page.add_button.click()
            common.take_screenshot('點擊加號')

        with allure.step('點擊數字9'):
            calculator_page.number_9_button.click()
            common.take_screenshot('點擊數字9')

        with allure.step('點擊等於'):
            calculator_page.equal_button.click()
            common.take_screenshot('點擊等於')

        with allure.step('驗證結果'):
            actual_result = calculator_page.result_field.text
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '17'

    @allure.story('加法測試')
    @allure.title('[case02]加法測試')
    @pytest.mark.add_sub_basic
    def test_add_case02(self, open_app, close_app):

        driver = open_app
        common = Common(driver)
        calculator_page = CalculatorPage(driver)

        with allure.step('點擊數字5'):
            calculator_page.number_5_button.click()
            common.take_screenshot('點擊數字5')

        with allure.step('點擊加號'):
            calculator_page.add_button.click()
            common.take_screenshot('點擊加號')

        with allure.step('點擊數字1'):
            calculator_page.number_1_button.click()
            common.take_screenshot('點擊數字1')

        with allure.step('點擊等於'):
            calculator_page.equal_button.click()
            common.take_screenshot('點擊等於')

        with allure.step('驗證結果'):
            actual_result = calculator_page.result_field.text
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '6'
