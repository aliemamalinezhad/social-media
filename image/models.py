from utils.general_model import GeneralModel
from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField, PPOIField


# Create your models here.

class Image(GeneralModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name
