import os
import django
from random import randint
from datetime import datetime, timedelta
from dandhacontrol.models import Service, PaymentMode, Client, Company, CompanyServiceRelationship, Locality, Customer, Package, Device, Recharge


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
# django.setup()


# Create some services

from django.core.management.base import BaseCommand


def insert_dummy_data():
    service1 = Service.objects.create(name='Internet')
    service2 = Service.objects.create(name='Cable TV')
    service3 = Service.objects.create(name='Phone')

    # Create some payment modes
    payment_mode1 = PaymentMode.objects.create(name='Cash')
    payment_mode2 = PaymentMode.objects.create(name='Credit Card')
    payment_mode3 = PaymentMode.objects.create(name='Debit Card')

    # Create some clients
    client1 = Client.objects.create(client_auth_id='12345', client_name='John Doe')
    client2 = Client.objects.create(client_auth_id='54321', client_name='Jane Smith')

    # Create some localities
    locality1 = Locality.objects.create(area='Downtown', client=client1)
    locality2 = Locality.objects.create(area='Suburbs', client=client2)

    # Create some customers
    customer1 = Customer.objects.create(customer_name='Bob',
                                        text_address={'street': '123 Main St', 'city': 'Anytown', 'state': 'CA',
                                                      'zip': '12345'}, client=client1, locality=locality1)
    customer2 = Customer.objects.create(customer_name='Alice',
                                        text_address={'street': '456 Elm St', 'city': 'Anytown', 'state': 'CA',
                                                      'zip': '12345'}, client=client2, locality=locality2)

    # Create some companies
    company1 = Company.objects.create(company_name='ABC', client=client1)
    company2 = Company.objects.create(company_name='XYZ', client=client2)

    # Add services to companies
    CompanyServiceRelationship.objects.create(service_info=service1, company_info=company1)
    CompanyServiceRelationship.objects.create(service_info=service2, company_info=company1)
    CompanyServiceRelationship.objects.create(service_info=service3, company_info=company2)

    # Create some packages
    package1 = Package.objects.create(name='Basic', price_monthly=50,
                                      company_service_info=CompanyServiceRelationship.objects.first())
    package2 = Package.objects.create(name='Premium', price_monthly=100,
                                      company_service_info=CompanyServiceRelationship.objects.last())

    # Create some devices
    device1 = Device.objects.create(device_number='1234567890', package=package1, locality=locality1,
                                    customer=customer1, add_on_price=10, status=Device.ACTIVE,
                                    recharge_date=datetime.now().date() + timedelta(days=30), balance=50)
    device2 = Device.objects.create(device_number='0987654321', package=package2, locality=locality2,
                                    customer=customer2, add_on_price=20, status=Device.ACTIVE,
                                    recharge_date=datetime.now().date() + timedelta(days=30), balance=100)

    # Create some recharges
    recharge1 = Recharge.objects.create(device=device1, payment_collected=Recharge.YES, payment_amount=50,
                                        payment_date=datetime.now().date(), recharge_entry=datetime.now().date(),
                                        payment_mode=payment_mode1)
    recharge2 = Recharge.objects.create(device=device2, payment_collected=Recharge.NO,
                                        payment_date=datetime.now().date(), recharge_entry=datetime.now().date(),
                                        payment_mode=payment_mode2)
    recharge2 = Recharge.objects.create(device=device2, payment_collected=Recharge.NO,
                                        payment_date=datetime.now().date(), recharge_entry=datetime.now().date(),
                                        payment_mode=payment_mode2)
    recharge2 = Recharge.objects.create(device=device2, payment_collected=Recharge.NO,
                                        payment_date=datetime.now().date(), recharge_entry=datetime.now().date(),
                                        payment_mode=payment_mode2)


class Command(BaseCommand):
    help = 'Inserts dummy data into the database'

    def handle(self, *args, **options):
        insert_dummy_data()
