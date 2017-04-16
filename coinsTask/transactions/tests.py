from rest_framework.test import APITestCase
from customer.models import UserAccount
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from transactions.views import PaymentAPI
import json

class PaymentsTestCase(APITestCase):
    url = "/v1/payments/"

    def setUp(self):
        self.u1 = User.objects.create_user(
            username='alice', email='alice@coins.ph', password='alice')
        self.u2 = User.objects.create_user(
            username='bob', email='bob@coins.ph', password='bob')
                

    def test_payments_post_api(self):

        # fetch user accounts
        ua1 = UserAccount.objects.get(user=self.u1)
        ua2 = UserAccount.objects.get(user=self.u2)

        # make POST request
        factory = APIRequestFactory()
        view = PaymentAPI.as_view()
        data = {
            "amount": 105.5,
            "from_account": str(ua1.guid),
            "to_account": str(ua2.guid),
            "initiated_by": str(ua1.guid),
        }
        request = factory.post(self.url, json.dumps(data), content_type='application/json')
        response = view(request)
        response.render()
        
        # refresh user account variables
        ua1.refresh_from_db()
        ua2.refresh_from_db()

        # check for balances and status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ua1.balance, -105.5)
        self.assertEqual(ua2.balance, 105.5)

        # check GET API
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

