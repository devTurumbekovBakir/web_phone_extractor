import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import phonenumbers


def fetch_page_with_selenium(url):
    """
    Получает содержимое веб-страницы с использованием Selenium для обработки динамического контента.

    Параметры:
    - url (str): URL веб-страницы.

    Возвращает:
    - str: HTML-содержимое страницы.
    """
    try:
        # Менеджер контекста для гарантии закрытия драйвера даже при возникновении исключения
        with webdriver.Chrome() as driver:
            driver.get(url)
            time.sleep(2)

            # Найти и нажать кнопку
            show_phone_button = driver.find_element(By.XPATH, '//button[contains(@class, "phone-number_hidden")]')
            show_phone_button.click()
            time.sleep(2)

            return driver.page_source

    except Exception as e:
        print(f"Ошибка при извлечении страницы из {url}: {e}")
        return None


def fetch_page(url):
    """
    Получает содержимое веб-страницы с использованием библиотеки requests.

    Параметры:
    - url (str): URL веб-страницы.

    Возвращает:
    - str: HTML-содержимое страницы.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при извлечении страницы из {url}: {e}")
        return None


def extract_phone_numbers(html):
    """
    Извлекает номера телефонов из HTML-содержимого с использованием BeautifulSoup и библиотеки phonenumbers.

    Параметры:
    - html (str): HTML-содержимое страницы.

    Возвращает:
    - set: Множество отформатированных номеров телефонов.
    """
    soup = BeautifulSoup(html, 'html.parser')
    phone_numbers = set()

    for tag in soup.find_all(['p', 'span', 'div', 'a']):
        text = tag.get_text()
        for match in phonenumbers.PhoneNumberMatcher(text, 'RU'):
            phone_numbers.add(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

    return phone_numbers


def main():
    """
    Основная функция для сканирования номеров телефонов на списке URL.
    """
    urls = ['https://hands.ru/company/about', 'https://repetitors.info']

    for url in urls:
        print(f"Сканирование {url} номеров телефонов...")

        if "hands.ru" in url:
            page_content = fetch_page_with_selenium(url)
        else:
            page_content = fetch_page(url)

        if page_content:
            phone_numbers = extract_phone_numbers(page_content)
            if phone_numbers:
                print(f"Найдены номера телефонов на {url}:")
                for number in phone_numbers:
                    print(number)
            else:
                print("Номера телефонов не найдены.")
        print("\n")


if __name__ == "__main__":
    main()
