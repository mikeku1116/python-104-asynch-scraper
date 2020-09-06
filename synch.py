from bs4 import BeautifulSoup
import requests
import time


start_time = time.time()  # 開始時間

for page in range(1, 11):  # 爬取1-10頁

    response = requests.get(
        "https://www.104.com.tw/jobs/search/?keyword=python&order=1&page=" + str(page) + "&jobsource=2018indexpoc&ro=0")
    soup = BeautifulSoup(response.content, "lxml")  # 解析HTML原始碼

    blocks = soup.find_all("div", {"class": "b-block__left"})  # 職缺區塊
    for block in blocks:

        job = block.find("a", {"class": "js-job-link"})  # 職缺名稱
        if job is None:
            continue

        company = block.find_all("li")[1]  # 公司名稱
        salary = block.find("span", {"class": "b-tag--default"})  # 待遇

        print((job.getText(),) + (company.getText().strip(),) + (salary.getText(),))

print("花費：" + str(time.time() - start_time) + "秒")
