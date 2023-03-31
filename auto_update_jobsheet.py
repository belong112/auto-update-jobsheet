import requests
import datetime
from bs4 import BeautifulSoup
import pygsheets
import re


def getCompanyId(url):
    match = re.search(r'(?<=company\/)[a-zA-Z0-9]+', url)
    return match.group(0)


def write_into_sheet():
    auth_file = "google-sheet-access-key.json"
    gc = pygsheets.authorize(service_file=auth_file)
    sheet_url = "https://docs.google.com/spreadsheets/d/11DP1bPkGvImaAAi6lVFcXyZGWdMdEJy-7OTyXUXX3_s"
    global_sheet = gc.open_by_url(sheet_url)
    sheet_work01 = global_sheet.worksheet_by_title("work01")
    company_urls = (sheet_work01.get_col(6, include_tailing_empty=False))
    for row_id, c_url in enumerate(company_urls):
        url = c_url
        if "104.com.tw" not in url:  # 目前只能爬 104 的網站
            continue
        selected = []
        for _ in range(3):  # 一頁20筆資料，最多抓60筆
            r = requests.get(url)  # 將網頁資料GET下來
            soup = BeautifulSoup(r.text,"html.parser")  # 將網頁資料以 html.parser
            # company_name = soup.select("h1")[0].text  # 取出公司名稱
            selected += soup.select("div.info-job")  # 取所有HTML標中的 <div class="info-job">*職缺名稱*</div>標籤存入sel
            footer = soup.select("div.joblist__footer a")
            if footer and url != "https://www.104.com.tw" + footer[-1]['href']:
                url = "https://www.104.com.tw" + footer[-1]['href']  # 抓下一頁的網址
            else:
                break

        # 資料處理完畢後再寫入表格
        sheet_work01.update_value('d' + str(row_id+1),  concludeChatGPT(selected))  # 將歸納後的職業寫入表格
        # sheet_work01.update_value('d' + str(row_id+1),  '\n'.join([x.text for x in selected]))  # 將歸納後的職業寫入表格 測試用
        sheet_work01.update_value('g' + str(row_id+1), str(datetime.date.today()))  # 將更新日期寫入表格


def concludeChatGPT(jobs):
    #open text file in read mode
    api_file = open("open-ai-access-key.txt", "r")
    api_key = api_file.read().rstrip()
    prompt = '請將下述職業\n\n' + '\n'.join([x.text for x in jobs]) + '\n\n歸納成五項職業，越精簡越好'

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        },
        json={
            'model': 'gpt-3.5-turbo', # 一定要用chat可以用的模型
            'messages': [{"role": "user", "content": prompt}]
        })

    # 使用json解析
    json = response.json()
    return json['choices'][0]['message']['content']

# class google_sheet_helper:
#     def __init__(self, sheet_name = "work01"):
#         # setting sheet
#         self.working_sheet = global_sheet.worksheet_by_title(sheet_name)

#     def write(self, position = "A1", content = "test"):
#         self.working_sheet.update_value(position, content)

#     def read(self, position = "A1"):
#         content = self.working_sheet.cell(position)
#         print(content)
#         print(content.value)

#     def append(self, values = []):
#         self.working_sheet.append_table(values=values)

#     def insert(self, insert_rows = 1, values = []): # insert_rows = 1, start from 2
#         self.working_sheet.insert_rows(insert_rows, number=1, values=values)
    
write_into_sheet()
