from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# 業種とURLの辞書
categories = {
    "グルメ・飲食": "https://listoss.com/search.php?category_big=グルメ・飲食",
    "ショッピング": "https://listoss.com/search.php?category_big=ショッピング",
    "ビジネス": "https://listoss.com/search.php?category_big=ビジネス",
    "ペット": "https://listoss.com/search.php?category_big=ペット",
    "レジャー・スポーツ": "https://listoss.com/search.php?category_big=レジャー・スポーツ",
    "医療・健康・介護": "https://listoss.com/search.php?category_big=医療・健康・介護",
    "冠婚葬祭・イベント": "https://listoss.com/search.php?category_big=冠婚葬祭・イベント",
    "教育・習い事": "https://listoss.com/search.php?category_big=教育・習い事",
    "公共機関・団体": "https://listoss.com/search.php?category_big=公共機関・団体",
    "自動車・バイク": "https://listoss.com/search.php?category_big=自動車・バイク",
    "趣味": "https://listoss.com/search.php?category_big=趣味",
    "住まい": "https://listoss.com/search.php?category_big=住まい",
    "美容・ファッション": "https://listoss.com/search.php?category_big=美容・ファッション",
    "暮らし": "https://listoss.com/search.php?category_big=暮らし",
    "旅行宿泊": "https://listoss.com/search.php?category_big=旅行宿泊"
}

# ChromeDriverセットアップ（ヘッドレス）
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# データ格納用
all_data = []

for category, url in categories.items():
    print(f"🔍 {category} を取得中...")
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    rows = soup.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 6:
            company_name = cols[0].get_text(strip=True)
            address = cols[1].get_text(strip=True)
            phone = cols[2].get_text(strip=True)
            fax = cols[3].get_text(strip=True)
            source_url = cols[4].find('a')['href'] if cols[4].find('a') else ''
            category_label = cols[5].get_text(strip=True)

            all_data.append({
                '会社名': company_name,
                '住所': address,
                '電話番号': phone,
                'FAX番号': fax,
                '出典URL': source_url,
                'カテゴリ': category,
                'サブカテゴリ': category_label
            })

# データフレーム化
df = pd.DataFrame(all_data)

# CSV保存
filename = "全業種法人リスト.csv"
df.to_csv(filename, index=False, encoding='utf-8-sig')

print(f"✅ 保存完了: {os.path.abspath(filename)}")

driver.quit()


           
