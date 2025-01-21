import unittest
from unittest.mock import MagicMock, patch
from app import app

class TestVoteApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("app.redis_client")  # Simula el cliente Redis
    def test_vote_submission(self, mock_redis):
        # Simula el método rpush de Redis
        mock_redis.rpush = MagicMock()

        # Simula un formulario POST con el voto "Cats"
        response = self.app.post("/", json={"vote": "Cats"})

        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Received vote for Cats", response.data)

        # Verifica que se haya llamado al método rpush de Redis
        mock_redis.rpush.assert_called_once_with("votes", "Cats")

    def test_page_load(self):
        # Simula una solicitud GET
        response = self.app.get("/")

        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

#import unittest
#from app import app

#class TestVoteApp(unittest.TestCase):
#    def setUp(self):
#        self.app = app.test_client()
#        self.app.testing = True

#    def test_vote_submission(self):
        # Simular un formulario POST con el voto "Cats"
#        response = self.app.post("/", data={"vote": "Cats"})

        # Verificar que el código de estado sea 200
#        self.assertEqual(response.status_code, 200)

#    def test_page_load(self):
        # Simular una solicitud GET
#        response = self.app.get("/")

        # Verificar que el código de estado sea 200
#        self.assertEqual(response.status_code, 200)
        
#if __name__ == '__main__':
#    unittest.main()
