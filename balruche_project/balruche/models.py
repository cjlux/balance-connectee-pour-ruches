
from django.db import models
from django.conf import settings

class Site(models.Model):
  
  name = models.CharField("nom", max_length=100)
  
  def __str__(self):
    mess = f"Site: {self.name}"
    return mess
  
class Balance(models.Model):
  
  serial = models.CharField("nom", max_length=30, unique=True, )
  tared  = models.BooleanField("tarée", default=False)
  active = models.BooleanField("active", default=False)

  def info(self):
    mess = f"Balance <{self.serial}> "
    used = False
    for bal in ('bal_1', 'bal_2', 'bal_3', 'bal_4'):
      if hasattr(self, bal):
        mess += f" est '{bal}' dans la MasterBox <{getattr(self, bal).serial}>"
        used = True
    if not used:
      mess += "n'est utilisée par aucune MasterBox"
    return mess

  def __str__(self):
    mess = f"N° série: {self.serial}"
    return mess

class MasterBox(models.Model):
  
  IMEI     = models.CharField("IMEI", max_length=20, unique=True, )
  active   = models.BooleanField("active", default=False)
  GPS_latt = models.FloatField("Lattitude GPS", default=0.0)
  GPS_long = models.FloatField("Longitude GPS", default=0.0)
  bal_1 = models.OneToOneField(Balance, on_delete=models.SET_NULL, null=True, related_name='bal_1')
  bal_2 = models.OneToOneField(Balance, on_delete=models.SET_NULL, null=True, related_name='bal_2')
  bal_3 = models.OneToOneField(Balance, on_delete=models.SET_NULL, null=True, related_name='bal_3')
  bal_4 = models.OneToOneField(Balance, on_delete=models.SET_NULL, null=True, related_name='bal_4')

  def info(self):
    mess = ""
    mess += f"MasterBox <{self.IMEI}> :\n"
    for bal in ('bal_1', 'bal_2', 'bal_3', 'bal_4'):
      mess += f"\t '{bal}' "
      if getattr(self, bal) == None:
        mess += f"n'est pas installée \n"
      else:
        mess += f" <{getattr(self, bal).serial}> tarée:{getattr(self, bal).tared} active:{getattr(self, bal).active} \n"
    return mess
    
    
  def __str__(self):
    mess = f"IMEI: {self.IMEI}"
    return mess
  
class BalRucheData(models.Model):
  
  timestamp = models.DateTimeField('date_heure', auto_now_add=True)
  week_num  = models.IntegerField('N° semaine', default=0, db_index=True)
  day_num   = models.IntegerField('N° jour', default=0, db_index=True)
  humid = models.IntegerField('humidité (%)', default=0)
  temp  = models.IntegerField('température (°C)', default=0)
  masse_ruche1 = models.FloatField("Masse ruche-1", default=0)
  masse_ruche2 = models.FloatField("Masse ruche-2", default=0)
  masse_ruche3 = models.FloatField("Masse ruche-3", default=0)
  masse_ruche4 = models.FloatField("Masse ruche-4", default=0)
  masterbox = models.ForeignKey(MasterBox, on_delete=models.PROTECT)
  
  def info(self):
    
    if hasattr(self,'masterbox'):
      mess = f"BalRucheData from MasterBoX_IMEI={self.masterbox.IMEI}\n"
    else:
      mess = f"BalRucheData from MasterBoX_UNKNOWN\n"
      
    mess += f"\ttimestamp={self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\tweek_num={self.week_num}\n\tday_num={self.day_num}\n"
    mess += f"\thumid={self.humid}\n\ttemp={self.temp}\n"
    mess += f"\tmasse_ruche1={self.masse_ruche1:.2f}\n\tmasse_ruche2={self.masse_ruche2:.2f}\n"
    mess += f"\tmasse_ruche3={self.masse_ruche3:.2f}\n\tmasse_ruche4={self.masse_ruche4:.2f}\n"
    return mess
    
  def __str__(self):
    mess = f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} from {self.masterbox.IMEI}"
    return mess
 
 