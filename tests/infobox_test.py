import unittest
import wikipedia


class TestLang(unittest.TestCase):
    """Test the ability for wikipedia to change the language of the API being accessed."""

    def test_infobox(self):
        wikipedia.set_lang('zh')
        wikipedia.set_proxy({'http': 'http://localhost:1080', 'https': 'https://localhost:1080'})
        wikipedia.set_request_lang('zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7')
        rslt = wikipedia.infobox('弱智')
        print(rslt)
        self.assertIsNotNone(rslt)

