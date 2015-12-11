import random

class DerechoHabienteDumb():
    def __init__(self, data):
        self._data = data

    def request(self):
        response = { "derechoHabiente": bool(random.getrandbits(1)) }

        return response

class ExpedienteClinicoDumb():
    def __init__(self, data):
        self._data = data

    def request(self):
        response = { "numero": 0 }

        return response
