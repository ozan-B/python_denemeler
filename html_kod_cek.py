import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error:", response.status_code)

url = "https://hasanemresatilmis.com/2017/09/12/active-directory-nedir/s"
html_content = get_html(url)
print(html_content)  # Sayfanın HTML kodu
