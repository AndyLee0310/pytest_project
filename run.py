import pytest
from module import allure_operate

if __name__ == '__main__':
    
    pytest.main(['-v'])    # -v: 顯示詳細資訊
    allure_operate.output_allure_html_report()
