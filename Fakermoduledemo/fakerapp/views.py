from django.http import HttpResponse
from django.shortcuts import render
from .models import Studentdata
from faker import Faker
# Create your views here.

fdata=Faker()

def fake_data(request):
    record=[]
    for i in range(20):
        fake_name=fdata.name()
        fake_address=fdata.address()
        fake_email=fdata.email()
        fake_company=fdata.company()
        student=Studentdata.objects.get_or_create(Name=fake_name,Address=fake_address,Company=fake_company,
                                                  Email=fake_email)
        record.append(student)
    return render(request,'fakerapp/show.html',{'record':record})