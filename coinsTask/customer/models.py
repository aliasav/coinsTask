from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import logging
import string
import uuid
import random

logger = logging.getLogger(__name__)


# Extends of user model
# contains user accout information
class UserAccount(models.Model):
    """ Extension of User model. All customer account
     related information is stored here """

    # this model extends User
    user = models.OneToOneField(User)

    # account id generated according to username
    user_account_id = models.CharField(max_length=15, null=False, blank=False) 

    # primary key to be used throughtout the APIs
    guid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, primary_key=True)  

    CURRENCIES = (
        ("PHP", "Philippine Peso"),
        ("INR", "Indian Rupee"),
        ("USD", "US Dollors"),
    )

    currency = models.CharField(max_length=5, choices=CURRENCIES, null=True, blank=False)
    balance = models.FloatField(default=0)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s<--->%s<--->%s" %(self.user, self.guid, self.balance)

# creates user profile on POST SAVE for User model
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        logger.debug("instance: %s" %instance)
        account_id = instance.username + '-' + ''.join(random.choice(string.digits) for _ in range(5))
        user_profile = UserAccount.objects.create(  user=instance, 
                                                    user_account_id=account_id,
                                                    currency="PHP",)
        logger.debug("Profile created for user: %s" %(instance))

# post save connector
post_save.connect(create_user_profile, sender=User)
