import unittest
from SI507project5_code import *

class TestTumblrAPI(unittest.TestCase):
    def setUp(self):
        return

    def testHasCacheExpired(self):
        isExpired = has_cache_expired("2017-10-09 00:08:59.893171", 1)
        self.assertTrue(isExpired, True)
        return

    def testGetFromCache(self):
        creds_data = get_from_cache("/INFO", CREDS_DICTION)
        self.assertTrue(type(creds_data) is list)

        data = get_from_cache('HTTPS://API.TUMBLR.COM/V2/BLOG/?API_/POSTS_BLOG-IDENTIFIER_VINBEIGIE', CACHE_DICTION)
        self.assertTrue(type(data) is dict)
        return

    def testCreateRequestIdentifier(self):
        identifier = create_request_identifier('https://api.tumblr.com/v2/blog/', {'blog-identifier': 'peacecorps.tumblr.com', 'api': '/info'})
        self.assertEqual(identifier, 'HTTPS://API.TUMBLR.COM/V2/BLOG/?API_/INFO_BLOG-IDENTIFIER_PEACECORPS.TUMBLR.COM')
        return

    def testGetCachedDataFrom_api(self):
        data = get_data_from_api('https://api.tumblr.com/v2/blog/', {'api': '/info', 'blog-identifier': 'peacecorps.tumblr.com'})
        self.assertTrue(type(data) is dict)
        return

    def testGetCachedTokenFromService(self):
        token = get_tokens_from_service("/INFO")
        self.assertTrue(type(token) is list)
        return

if __name__ == "__main__":
    unittest.main(verbosity=2)
