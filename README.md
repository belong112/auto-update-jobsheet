# 自動化更新 TFT 職缺小站小工具

## 功能介紹

能自動爬蟲獲得各公司現有職缺，並透過 chatGPT 統整，並利用 pygsheets 將資訊更新至此 google sheet 上面

---

## 操作方式

clone 此專案到你的電腦

```
git clone "https://github.com/belong112/auto-update-jobsheet.git"
```

下載完檔案之後請至 open ai 獲得自己的 access code 然後將之放在專案資料夾內
，請創建一個 open-ai-access-key.txt 檔案，並將你獲得的 access key 輸入

```
cd auto-update-jobsheet
touch open-ai-access-key.txt
vim open-ai-access-key.txt
# 接著就自行貼上 access key
```

參考：[如何獲得 open-ai api access code](https://www.soft4fun.net/tech/ai/openai-api-key.htm)

加入後即可回到終端機執行

```
python auto_write_jobsheet.py
```

---

## 注意事項

### 欲新增新公司

可直接在表格中插入新公司，需注意職缺連結該欄位必須填寫「公司頁面」的網址，範例：https://www.104.com.tw/company/{公司id}

![image info](https://i.imgur.com/wkB6D0W.png)
需至此頁面複製網址

---

## 限制

目前只能抓 104 的資料，遇到非 104 的職缺網站需透過手動方式新增
