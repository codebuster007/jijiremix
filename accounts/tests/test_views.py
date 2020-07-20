import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserAccountTest(APITestCase):

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

    def test_account_detail_retrieve_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/accounts/me/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_account_detail_retrieve_authenticated(self):
        response = self.client.get('/api/v1/accounts/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accounts_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/accounts/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_accounts_list_authenticated(self):
        response = self.client.get('/api/v1/accounts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
