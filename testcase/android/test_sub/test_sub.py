import allure
import pytest
import re
import logging
from module.common import Common
from page.calculator import CalculatorPage

@allure.feature('減法測試')
@allure.feature('v1.0')
class TestSub():

    @allure.story('減法測試')
    @allure.title('[case01]減法測試')
    @pytest.mark.add_sub_basic
    @pytest.mark.dev
    def test_sub_case01(self, open_app, close_app):
        driver = open_app
        common = Common(driver)
        calculator_page = CalculatorPage(driver)

        with allure.step('點擊數字8'):
            calculator_page.number_8_button.click()
            common.take_screenshot('點擊數字8')

        with allure.step('點擊減號'):
            calculator_page.sub_button.click()
            common.take_screenshot('點擊減號')

        with allure.step('點擊數字9'):
            calculator_page.number_9_button.click()
            common.take_screenshot('點擊數字9')

        with allure.step('點擊等於'):
            calculator_page.equal_button.click()
            common.take_screenshot('點擊等於')

        with allure.step('驗證結果'):
            actual_result = calculator_page.result_field.text
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '−1'

    @allure.story('減法測試')
    @allure.title('[case02]減法測試')
    @pytest.mark.add_sub_basic
    def test_sub_case02(self, open_app, close_app):

        driver = open_app
        common = Common(driver)
        calculator_page = CalculatorPage(driver)

        with allure.step('點擊數字568'):
            calculator_page.number_5_button.click()
            calculator_page.number_6_button.click()
            calculator_page.number_8_button.click()

            common.take_screenshot('點擊數字568')

        with allure.step('點擊減號'):
            calculator_page.sub_button.click()
            common.take_screenshot('點擊減號')

        with allure.step('點擊數字18'):
            calculator_page.number_1_button.click()
            calculator_page.number_8_button.click()
            common.take_screenshot('點擊數字1')

        with allure.step('點擊等於'):
            calculator_page.equal_button.click()
            common.take_screenshot('點擊等於')

        with allure.step('驗證結果'):
            actual_result = calculator_page.result_field.text
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '550'
