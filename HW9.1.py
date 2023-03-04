import urllib.request
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
usd_rate_urllib = float(eval(data)["rates"]["UAH"])

print("Курс долара зараз:", usd_rate_urllib)