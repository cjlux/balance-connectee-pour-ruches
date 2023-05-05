from django import forms
from balruche.models import BalRucheData

class ReceiveDataForm(forms.ModelForm):
    
    class Meta:
        model = BalRucheData
        exclude = ('timestamp', 'week_num', 'day_num', 'masterbox')
    
    IMEI     = forms.CharField(max_length=20)
    