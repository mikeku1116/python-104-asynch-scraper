from aiohttp import ClientSession
from bs4 import BeautifulSoup
import asyncio
import time


# 定義協程(coroutine)
async def main():
    links = list()
    for page in range(1, 11):
        links.append(
            f"https://www.104.com.tw/jobs/search/?keyword=python&order=1&page={page}&jobsource=2018indexpoc&ro=0")

    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(link, session)) for link in links]  # 建立任務清單
        await asyncio.gather(*tasks)  # 打包任務清單及執行


# 定義協程(coroutine)
async def fetch(link, session):
    async with session.get(link) as response:  # 非同步發送請求
        html_body = await response.text()

        soup = BeautifulSoup(html_body, "lxml")  # 解析HTML原始碼

        blocks = soup.find_all("div", {"class": "b-block__left"})  # 職缺區塊
        for block in blocks:

            job = block.find("a", {"class": "js-job-link"})  # 職缺名稱
            if job is None:
                continue

            company = block.find_all("li")[1]  # 公司名稱
            salary = block.find("span", {"class": "b-tag--default"})  # 待遇

            print((job.getText(),) + (company.getText().strip(),) +
                  (salary.getText(),))

start_time = time.time()  # 開始執行時間
loop = asyncio.get_event_loop()  # 建立事件迴圈(Event Loop)
loop.run_until_complete(main())  # 執行協程(coroutine)
print("花費:" + str(time.time() - start_time) + "秒")
