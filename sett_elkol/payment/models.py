from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from sett_elkol.common.models import TimeStampedUUIDModel

class payment_method(TimeStampedUUIDModel):
    card_number = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from="card_number", always_update=True, unique=True)
    Bank = models.CharField(max_length=30)
    
    
    
    