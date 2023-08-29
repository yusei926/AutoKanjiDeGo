import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

from pykakasi import kakasi

driver = webdriver.Chrome(ChromeDriverManager().install())

# # サイトにアクセス
# driver.get('https://html5.plicy.net/GamePlay/155561')
# time.sleep(3)

# elem = driver.find_element('xpath', '//*[@id="_111_input"]')
# elem.send_keys(Keys.RETURN)
# elem.send_keys(Keys.RETURN)

# text = "諭す"
# kks = kakasi()
# result = kks.convert(text)

# # ひらがなにする
# for converted_word in result:
#     hiragana = f"{converted_word['hira']}"

# print(hiragana)