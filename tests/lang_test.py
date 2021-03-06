# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia


class TestLang(unittest.TestCase):
    """Test the ability for wikipedia to change the language of the API being accessed."""

    def test_lang(self):
        wikipedia.set_lang("fr")
        self.assertEqual(wikipedia.API_URL, 'http://fr.wikipedia.org/w/api.php')

    def test_zh(self):
        wikipedia.set_lang('zh')
        wikipedia.set_proxy({'http': 'http://localhost:1080', 'https': 'https://localhost:1080'})
        wikipedia.set_request_lang('zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7')
        print(wikipedia.summary('流行性感冒'))
