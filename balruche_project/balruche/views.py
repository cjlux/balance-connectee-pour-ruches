from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from . import forms
from balruche.models import BalRucheData, MasterBox
from django.views.decorators.csrf import csrf_exempt

@login_required
def home(request):
    return render(request, 'balruche/home.html')

@csrf_exempt
def receive_data(request):
    
    if request.method == 'POST':
        print(request.POST)
        print("request.body:\n",request.body)
        print("request.headers:\n",request.headers)
        form = forms.ReceiveDataForm(request.POST)
        if form.is_valid():
            br_data = BalRucheData()
            br_data.timestamp    = datetime.now()
            br_data.week_num     = br_data.timestamp.isocalendar().week
            br_data.day_num      = br_data.timestamp.timetuple().tm_yday
            br_data.humid        = form.cleaned_data['humid']
            br_data.temp         = form.cleaned_data['temp']
            br_data.masse_ruche1 = form.cleaned_data['masse_ruche1']
            br_data.masse_ruche2 = form.cleaned_data['masse_ruche2']
            br_data.masse_ruche3 = form.cleaned_data['masse_ruche3']
            br_data.masse_ruche4 = form.cleaned_data['masse_ruche4']
            IMEI  = form.cleaned_data['IMEI']
            query = MasterBox.objects.filter(IMEI=IMEI)
            if query.count() == 0:
                print(f"received balruche_data for inexistant MasterBOX IME=<{IMEI}>")
            else:
                br_data.masterbox = query[0]
                br_data.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            print('invalid form')
    else:
        form = forms.ReceiveDataForm()
    return render(request, 'balruche/receive_data.html', context={'form': form})    
   
