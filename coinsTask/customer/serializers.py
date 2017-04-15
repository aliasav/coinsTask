from rest_framework import serializers
from customer.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('user', 'user_account_id', 'currency', 'balance', 'created_at', 'updated_at', 'guid')
        #depth = 1 # uncomment to include user details 