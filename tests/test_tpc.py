import unittest
from tpc import tpc


class TpcTest(unittest.TestCase):
    def test_get_authorization_url(self):
        client_id = 'client_id'
        redirect_uri = 'redirect_uri'
        expected = 'https://www.tistory.com/oauth/authorize?client_id=client_id&redirect_uri=redirect_uri&response_type=code'
        actual = tpc.get_authorization_url(client_id, redirect_uri)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
