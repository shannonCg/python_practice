import requests

www = requests.get("http://m.ftv.com.tw/newslist.aspx?class=L")
print(www.text)
