from __future__ import unicode_literals

from customer.models import UserAccount
from django.db import models
import uuid


# Payments model
class Payment(models.Model):
    """ Payment transactions model: Caters to incoming and outgoing transactions """

    guid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)  # primary key  
    
    # helps identify user who initiated the payment: can be extended to 
    # incorporate refunds
    initiated_by = models.ForeignKey(UserAccount, 
            related_name="payment_initiator")
    
    # from account: amount is deducted from this account
    from_account = models.ForeignKey(UserAccount, 
            related_name="from_account")    
    
    # to accout: amount is added to this accoutn
    to_account = models.ForeignKey(UserAccount, 
            related_name="to_account")    
    
    # amount of transaction
    amount = models.FloatField(null=True, blank=False)

    # True: In-coming
    # False: Out-going
    direction = models.BooleanField()

    # date time fields to track creation and updation 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __unicode__(self):
        return "%s<---->%s<---->%s" %(self.guid, self.from_account, self.to_account)

    def __str__(self):
        return "%s<---->%s<---->%s" %(self.guid, self.from_account, self.to_account)
