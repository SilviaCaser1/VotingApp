import unittest
from app import app

class TestVoteApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_vote_submission(self):
        # Simular un formulario POST con el voto "Cats"
        response = self.app.post("/", data={"vote": "Cats"})

        # Verificar que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

    def test_page_load(self):
        # Simular una solicitud GET
        response = self.app.get("/")

        # Verificar que el código de estado sea 200
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
