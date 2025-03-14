# 產生 allure report 且合併成獨立 html
import os
import logging
import allure_combine
from . import path

def output_allure_html_report():

    # 如果report資料夾不存在，則創建
    if not os.path.exists(path.REPORT):
        os.makedirs(path.REPORT)
        logging.info(f"'{path.REPORT}' 資料夾已創建")
    else:
        logging.info(f"'{path.REPORT}' 資料夾已存在")

    # 產生 html 報告
    os.system(f'allure generate {path.ALLURE_RESULTS} -o {path.ALLURE_REPORT} --clean')

    # 合併 allure report 成獨立 html
    allure_combine.combine_allure(path.ALLURE_REPORT)

    # 移動 complete.html 到 report 資料夾
    os.system(f'mv {path.ALLURE_REPORT}/complete.html {path.REPORT}')

    # 刪除 allure-report 資料夾
    os.system(f'rm -rf {path.ALLURE_REPORT}')
