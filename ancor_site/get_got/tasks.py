import os
import requests
import time
from django.conf import settings
from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from .models import *


@shared_task
def get_crypto_icons():
    url = "https://coinmarketcap.com/uk/"

    # Встановлення драйвера для Chrome
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")  # Запуск браузера в фоновому режимі
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    scroll_pause_time = 0.00001
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    last_height = driver.execute_script("return window.scrollY")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return window.scrollY")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    directory = os.path.join(settings.MEDIA_ROOT, "crypto_icons")
    if not os.path.exists(directory):
        os.makedirs(directory)

    images = soup.find_all("img", class_="coin-logo")

    max_images = 100
    for i, img in enumerate(images):
        if i >= max_images:
            break
        img_url = img["src"]
        img_name = img["alt"].replace(" ", "").replace('logo', '') + ".png"
        img_path = os.path.join(directory, img_name)

        # Завантажити зображення
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)

        # Збереження інформації про зображення в базі даних
        # Image.objects.create(url=img_url, name=img_name)
