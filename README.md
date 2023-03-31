# 自動化更新 TFT 職缺小站小工具

## 功能介紹

能自動爬蟲獲得各公司現有職缺，並透過 chatGPT 統整，並將資訊更新至此 google sheet 上面

---

## 操作方式

_給不會程式的你：_
請到右上角按下載

_給會程式的你：_
clone 此專案到你的電腦

> git clone "https://github/belong112

執行

> cd auto-update-jobsheet
> python auto_write_jobsheet.py

---

## 注意事項

下載完檔案之後請至 open ai 獲得自己的 access code 然後將之放在專案資料夾內
，再將該檔案改名為：openai-access-key.txt

---

## 更新方式

### 欲新增新公司與職缺

可直接在表格中插入新公司，需注意職缺連結該欄位必須填寫「公司頁面」的網址，範例：https://www.104.com.tw/company/{公司id}

![image info](https://i.imgur.com/wkB6D0W.png)
需至此頁面複製網址

### 啟動方式

開啟 terminal

---

## 限制

目前只能抓 104 的資料，遇到非 104 的職缺網站需透過手動方式新增
