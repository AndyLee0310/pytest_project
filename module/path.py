# 放置路徑相關資料
import os

BASE = os.path.dirname(os.path.dirname(__file__))
REPORT = os.path.join(BASE, 'report')
ALLURE_RESULTS = os.path.join(REPORT, 'allure-results')
ALLURE_REPORT = os.path.join(REPORT, 'allure-report')
