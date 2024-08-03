import requests

url = 'https://www.sogou.com/web?query=周杰伦'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

resp = requests.get(url, headers=headers)
print(resp.text)