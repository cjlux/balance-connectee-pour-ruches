from django import forms
from balruche.models import BalRucheData

class ReceiveDataForm(forms.ModelForm):
    
    class Meta:
        model = BalRucheData
        exclude = ('timestamp', 'w_num', 'd_num', 'masterbox')
    
    IMEI     = forms.CharField(max_length=20)
    