import unittest
from unittest.mock import patch
from main import fetch_page_with_selenium, fetch_page, extract_phone_numbers


class TestWebScraper(unittest.TestCase):
    @patch('builtins.print', side_effect=lambda *args, **kwargs: None)
    def test_fetch_page_with_selenium(self, mock_print):
        url = 'https://hands.ru/company/about'
        page_content = fetch_page_with_selenium(url)
        self.assertIsNotNone(page_content)

    def test_fetch_page(self):
        url = 'https://repetitors.info'
        page_content = fetch_page(url)
        self.assertIsNotNone(page_content)

    def test_extract_phone_numbers(self):
        html = '<html><body><p>Phone: +1 123-456-7890</p></body></html>'
        phone_numbers = extract_phone_numbers(html)
        self.assertNotIn('+11234567890', phone_numbers)


if __name__ == '__main__':
    unittest.main()
