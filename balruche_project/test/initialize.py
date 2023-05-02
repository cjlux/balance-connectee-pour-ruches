from authentication.models import User
from balruche.models import Site, MasterBox, Balance, BalRucheData

u=User.objects.create_user('PJT@free.fr', 'balruche')
u.save()

site=Site.objects.create(name="st médard")
site.save()
print(site) 

b=Balance(serial='b_0001')
b.save()
b=Balance(serial='b_0002')
b.save()
b=Balance(serial='b_0003')
b.save()
b=Balance(serial='b_0004')
b.save()

mb1=MasterBox(IMEI='864735053265720')
mb1.save()
mb1.bal_1=Balance.objects.all()[0]
mb1.bal_2=Balance.objects.all()[1]
mb1.bal_3=Balance.objects.all()[2]
mb1.bal_4=Balance.objects.all()[3]

mb2=MasterBox(IMEI='284735053265720')
mb2.save()
mb2.bal_1=Balance.objects.all()[0]
mb2.save()
