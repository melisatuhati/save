from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://geonode_y9cN7qjfl0:57b054b4-a149-497e-b98c-9dae574bfbfc@proxy.geonode.io:10012',
        'https': 'https://geonode_y9cN7qjfl0:57b054b4-a149-497e-b98c-9dae574bfbfc@proxy.geonode.io:10012',
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

driver.get("https://sepolia-faucet.pk910.de/#/mine/75dfdb41-32d6-45cb-a760-98fdf8bc3ee9")
time.sleep(50)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
