import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ItemViewTest(APITestCase):

    def setUp(self):
        account_data = {
            'email': 'johndoe@gmail.com',
            'password': 'issa-boat-issa-plane',
            'first_name': 'john',
            'last_name': 'doe',
            'residence_state': 'lagos',
        }

        # create a new user, post request to djoser
        self.user = self.client.post('/api/v1/accounts/', data=account_data)
        # Login a user
        response = self.client.post('/api/v1/accounts/login/', data={'email':'johndoe@gmail.com',
                               'password':'issa-boat-issa-plane'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
    
    def test_create_store_item(self):
        data = {
            'name': 'S9+ Foriegn used',
            'description': 'Clean UK used S9+',
            'price': 140000.0
        }
        item = self.client.post('/api/v1/store/', data=data)

        self.assertEqual(item.status_code, status.HTTP_201_CREATED)
    
    def test_create_buyer_for_item(self):
        data = {
            'name': 'S9+ Foriegn used',
            'description': 'Clean UK used S9+',
            'price': 140000.0
        }
        item = self.client.post('/api/v1/store/', data=data)
        item_id = item.data['item_id']

        self.client.force_authenticate(user=None)
        buyer_data = {
            "name": "joseph doe",
            "email": "josephdoe@yahoo.com",
            "location": "abuja"
        }
        interested_url = "/api/v1/store/{}/interested/".format(item_id)
        buyer = self.client.post(interested_url, data=json.dumps(buyer_data), content_type="application/json")

        self.assertEqual(buyer.status_code, status.HTTP_201_CREATED)
