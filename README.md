# python-104-asynch-scraper #

## 專案介紹 ##

本專案為104人力銀行的Python網頁爬蟲，取得Python相關的職缺名稱、公司名稱及待遇，包含同步(Synchronous)及非同步(Asynchronous)的寫法，其中，非同步(Asynchronous)的部分，asynch.py檔案使用GRequests套件，來平行發送請求(request)，可以搭配[[Python爬蟲教學]非同步爬蟲使用GRequests套件提升爬取效率的實作技巧](https://www.learncodewithmike.com/2020/09/python-asynchronous-scraper-using-grequests.html)部落格文章來進行學習。而asynch2.py檔案則整合asyncio及aiohttp模組(Module)來進行非同步的開發，可以搭配[[Python爬蟲教學]整合asyncio與aiohttp打造Python非同步網頁爬蟲](https://www.learncodewithmike.com/2020/09/python-asynchronous-scraper-using-asyncio-and-aiohttp.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境：

`$ pipenv shell`

登入後，就能夠執行同步(synch.py)及非同步(asynch.py)的Python網頁爬蟲。