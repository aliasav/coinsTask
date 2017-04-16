from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from customer.models import UserAccount

class AccountsTestCase(APITestCase):
    """ tests for customer app and APIs """
    
    url = "/v1/accounts/"

    def setUp(self):
        # create 2 users
        User.objects.create_user(
            username='daenerys', email='daenerys@esos.com', password='khaleesi')
        User.objects.create_user(
            username='jon_snow', email='jon_snom@thewall.com', password='iKnowNothing')

    def test_accounts_get_api(self):
        # test get accounts API        
        response = self.client.get(self.url)
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_default_balances(self):
        response = self.client.get(self.url)
        data = response.data
        for d in data:
            self.assertEqual(d.get("balance"), 0.0)
        