import os

class Config:
    PORT = int(os.getenv('PORT', '3000'))
    API_URL = os.getenv('API_URL', 'http://localhost:8000')
    API_TOKEN = os.getenv('API_TOKEN', '')
