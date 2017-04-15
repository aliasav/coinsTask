from rest_framework import serializers
from transactions.models import Payment
from customer.models import UserAccount

import logging

logger = logging.getLogger(__name__)


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    """ Payment model serializer """
    
    class Meta:
        model = Payment
        fields = ('guid', 'initiated_by', 'from_account', 'to_account', 'amount', 'direction', 'created_at', 'updated_at')

    def __fetch_user_account(self, guid):
        """ fetches a user accoutn object using guid """

        try:
            user_account = UserAccount.objects.get(guid=guid)
        except Exception as e:
            logger.exception(e)
        else:
            return user_account

    def __update_user_account(self, guid, amount, direction):
        """ updates a user account: amount is dedected/added from accout 
        based on direction """

        user_account = self.__fetch_user_account(guid=guid)
        if direction==True:
            user_account.balance += amount
        elif direction==False:
            user_account.balance -= amount
        else:
            return None
        
        user_account.save()
        logger.info("Updated user account: %s" %user_account)
        return user_account


    def __create_payment_object(self, data, direction):
        """ creates a payment object """

        from_account = self.__fetch_user_account(guid=data.get("from_account"))
        to_account = self.__fetch_user_account(guid=data.get("to_account"))
        payment_obj = Payment.objects.create(
            from_account=from_account,
            to_account=to_account,
            initiated_by=from_account,
            amount=data.get("amount"),
            direction=direction,
            )
        return payment_obj

    def create_incoming_payment(self, data):
        """ public method for incoming payment object creation """

        payment_obj = self.__create_payment_object(data=data, direction=True)
        self.__update_user_account(guid=data.get("to_account"), amount=data.get("amount"), direction=True)
        return payment_obj
 
    def create_outgoing_payment(self, data):
        """ public method for outgoing payment object creation """

        payment_obj = self.__create_payment_object(data=data, direction=False)
        self.__update_user_account(guid=data.get("from_account"), amount=data.get("amount"), direction=False)
        return payment_obj