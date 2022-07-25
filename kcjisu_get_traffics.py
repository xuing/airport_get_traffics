import os
import cloudscraper

def login(email, password):
    headers = {
        "User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh,zh-CN;q=0.9,en;q=0.8,ja;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    login_url = "https://"+os.environ["KCJISU_DOMAIN"]+"/auth/login"
    login_data = {
        "email": email,
        "passwd": password,
    }
    s = cloudscraper.create_scraper()
    s.post(url=login_url, data=login_data, headers=headers)
    return s

def get_traffic(s):
    headers = {
        "User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    gourl = "https://"+os.environ["KCJISU_DOMAIN"]+"/user/checkin"
    res = s.post(url=gourl, headers=headers,verify=False)
    print(res)
    print(res.json())


if __name__ == "__main__":
    email = os.environ["KCJISU_EMAIL"]
    password = os.environ["KCJISU_PASSWORD"]
    s = login(email,password)
    get_traffic(s)
    print("******************************")
