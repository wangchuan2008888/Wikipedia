import wikipedia
import unittest


class TestProxy(unittest.TestCase):
    def test_http_s(self):
        proxy = {
            'http': 'http://localhost:1080',
            'https': 'https://localhost:1080',
        }
        wikipedia.set_proxy(proxy)
        wikipedia.set_lang('zh')
        page = wikipedia.page('肥胖症')
        self.assertEqual(page.title, '肥胖症')

    def test_socks(self):
        proxy = {
            'http': 'socks5://localhost:1080',
            'https': 'socks5://localhost:1080',
        }
        wikipedia.set_proxy(proxy)
        wikipedia.set_lang('zh')
        page = wikipedia.page('肥胖症')
        self.assertEqual(page.title, '肥胖症')
