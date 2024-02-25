import time

import requests

word1 = "Fire"
word2 = "Water"
url = f"https://neal.fun/api/infinite-craft/pair?first={word1}&second={word2}"
print(url)
data = requests.get(url)
print(data.text)
