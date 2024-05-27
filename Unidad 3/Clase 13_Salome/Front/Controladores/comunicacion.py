import requests

class Comunicacion():
        
        def __init__(self, root):
            self.url = 'http://localhost:8000/v1/papitas'
            self.root = root
            pass

        