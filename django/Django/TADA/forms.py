from  django.forms import ModelForm
from .models import TaDa
from TADA.models import *

class UpdateTada(ModelForm):
    '''this class is for updating paid status'''
    class Meta:
        model=TaDa
        fields=['paid']
