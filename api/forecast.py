import re
import requests
from bs4 import BeautifulSoup

def main(url):
    # 解析済みのhtmlデータ
    s = soup(url)
    # result = s.find_all('td')
    # keyとvalue格納用辞書
    response = ""
    # for i in result:
    #     response+=f"{result}"
    print(s.text)

def soup(url):
  # 権限付与

    # Cookieを取得
    cookies = browser.driver().get_cookies()
    # 取得したCookieをrequestsに渡す形に変換
    d = []
    for cookie in cookies:
      d[cookie["name"] ] = cookie["value"]

    r = requests.get(url, cookies=)
    html = r.text.encode(r.encoding)
    buf = BeautifulSoup(html, 'html.parser')
    return buf

if __name__ == '__main__':
    # けんｋ
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSfVbUU-R2Jfizl_qK5pokotGJ9YyRQ2g_a79tkDDvgtAJGjfA/viewanalytics?pli=1&pli=1&pli=1'
    main(url)