import os
import pytest
import module.allure_operate as allure_operate

# current_path = os.path.dirname(__file__)

# json_report_path = os.path.join(current_path, 'report/json')
# html_report_path = os.path.join(current_path, 'report/html')


if __name__ == '__main__':
    
    # # pytest.main()
    # pytest.main(['-v'])
    # os.system(f'allure generate {json_report_path} -o {html_report_path} --clean')

    # json_report_path = "report/allure-results"
    # html_report_path = "report/allure-report"

    # 执行 pytest 测试并生成 allure 结果
    pytest.main(['-v'])

    allure_operate.output_allure_html_report()

    # report_folder_path = 'report'



    # # 使用 allure 命令生成 HTML 报告
    # os.system(f'allure generate {json_report_path} -o {html_report_path} --clean')
    # # allure generate allure-results -o allure-report --clean

    # # 合并 allure 报告
    # allure_combine.combine_allure(html_report_path)

    # os.system('mv report/allure-report/complete.html report')
    # os.system('rm -rf report/allure-report')
