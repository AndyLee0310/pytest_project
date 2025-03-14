import os
import pytest

current_path = os.path.dirname(__file__)

json_report_path = os.path.join(current_path, 'report/json')
html_report_path = os.path.join(current_path, 'report/html')


if __name__ == '__main__':
    
    # pytest.main()
    pytest.main(['-v'])
    os.system(f'allure generate {json_report_path} -o {html_report_path} --clean')