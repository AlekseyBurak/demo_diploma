from src.enums.common import HttpErrorCodes


def test_api_framework(api_client):
    response1 = api_client.pet.get_pet_by_id(1)
    assert response1.status_code == HttpErrorCodes.Content
    response2 = api_client.store.get_store_inventory()
    assert response2.status_code == HttpErrorCodes.Content



