<h1 align="center">Phone Number Scraper</h1>

<p align="center">
    <em>Этот скрипт предназначен для сканирования веб-страниц на наличие телефонных номеров с использованием 
        <code>requests</code> и <code>selenium</code> для обработки динамического контента. Он извлекает номера 
        телефонов из HTML-контента с помощью <code>BeautifulSoup</code> и библиотеки <code>phonenumbers</code>.
    </em>
</p>

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `selenium`
- `phonenumbers`
- ChromeDriver (для Selenium)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devTurumbekovBakir/web_phone_extractor.git
   cd web_phone_extractor
Установите необходимые пакеты Python:

bash
Copy code
pip install -r requirements.txt
Загрузите ChromeDriver и поместите его в каталог проекта:

Загрузка драйверов Chrome

Применение:
Запустите скрипт, выполнив:

bash
Copy code
python main.py
Скрипт просканирует список указанных URL-адресов на наличие телефонных номеров и отобразит отформатированные результаты.

go Сode
