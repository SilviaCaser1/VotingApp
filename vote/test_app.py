import unittest
from app import app

class TestVoteApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cats', response.data)
        self.assertIn(b'Dogs', response.data)

    def test_vote_submission(self):
        response = self.app.post('/', data={'vote': 'Cats'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for voting', response.data)

if __name__ == '__main__':
    unittest.main()
