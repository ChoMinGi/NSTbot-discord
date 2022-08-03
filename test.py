import requests
from bs4 import BeautifulSoup


def get():
    response = requests.get("http://munit.co.kr/lucky/today_proverb.php")
    soup = BeautifulSoup(response.content.decode(
        'utf-8', 'replace'), 'html.parser')
    main = soup.find("p").text
    if len(main) <= 100:
        print(main)
    else:
        print('repeat')
        get()


get()
