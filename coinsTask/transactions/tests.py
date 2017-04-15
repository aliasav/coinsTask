from rest_framework.test import APITestCase


class PaymentsTestCase(APITestCase):
    url = "/v1/payments/"
    def test_payments_get_api(self):        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)