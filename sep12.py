from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://sodagar:FGAMRHJ-QQHC7SJ-0RPJ3H1-BOMNLIP-WKACAQO-GWSCKMZ-SET2MG4@unmetered.residential.proxyrack.net:10144',
        'https': 'https://sodagar:FGAMRHJ-QQHC7SJ-0RPJ3H1-BOMNLIP-WKACAQO-GWSCKMZ-SET2MG4@unmetered.residential.proxyrack.net:10144',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920, 1200")
# Hapus '--headless' untuk melihat apakah ekstensi berjalan dengan benar dalam mode normal
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get('https://httpbin.org/ip')
print(driver.page_source)

time.sleep(1)

driver.get("https://sepolia-faucet.pk910.de/#/mine/8f9050da-9ef1-42f5-b2f0-08b80f5d4859")
time.sleep(50)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
