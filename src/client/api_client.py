from src.api.pet_api import PetApi
from src.api.store_api import StoreApi


class ApiClient:

    def __init__(self):
        self.pet: PetApi = PetApi()
        self.store: StoreApi = StoreApi()
