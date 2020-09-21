from customers.models import Customer
from leadership.models import Leadership
from authorities.models import Authoritie

class Generate(object):

    def statistic_customers(self):
        total = Customer.objects.count()

        #ADDRESS STATISTICS
        no_address_query = Customer.objects.filter(street='') | \
            Customer.objects.filter(street=None) | \
            Customer.objects.filter(number='') | \
            Customer.objects.filter(number=None) | \
            Customer.objects.filter(state='') | \
            Customer.objects.filter(state=None) | \
            Customer.objects.filter(cep='') | \
            Customer.objects.filter(cep=None) | \
            Customer.objects.filter(neighborhood='') | \
            Customer.objects.filter(neighborhood=None)
        no_address = no_address_query.count()
        address = total - no_address
        percentage_address = round((100*address)/total, 1)

        #PHONE STATISTICS
        no_phone_number = Customer.objects.filter(phone_number='') | \
            Customer.objects.filter(phone_number=None)
        no_cellphone = Customer.objects.filter(cellphone='') | \
            Customer.objects.filter(cellphone=None)
        no_phone_home = Customer.objects.filter(phone_home='') | \
            Customer.objects.filter(phone_home=None)

        no_phone_query = no_phone_number.intersection(no_cellphone).intersection(no_phone_home)
        no_phone = no_phone_query.count()
        phone = total - no_phone
        percentage_phone = round((100*phone)/total, 1)

        #EMAIL STATISTICS
        no_email = Customer.objects.filter(email='') | Customer.objects.filter(email=None)
        email = total - no_email.count()
        percentage_email = round((100*email)/total, 1)

        # BIRTH STATISTICS
        birth = Customer.objects.exclude(birth=None).count()
        percentage_birth = round((100*birth)/total, 1)



        customers = {'total': total,
                    'address': address,
                    'percentage_address': percentage_address,
                    'phone': phone,
                    'percentage_phone':percentage_phone,
                    'email': email,
                    'percentage_email': percentage_email,
                    'birth': birth,
                    'percentage_birth': percentage_birth}
        return customers

    def statistic_leadership(self):
        total = Leadership.objects.count()

        #ADDRESS STATISTICS
        no_address_query = Leadership.objects.filter(street='') | \
            Leadership.objects.filter(street=None) | \
            Leadership.objects.filter(number='') | \
            Leadership.objects.filter(number=None) | \
            Leadership.objects.filter(state='') | \
            Leadership.objects.filter(state=None) | \
            Leadership.objects.filter(cep='') | \
            Leadership.objects.filter(cep=None) | \
            Leadership.objects.filter(neighborhood='') | \
            Leadership.objects.filter(neighborhood=None)

        no_address = no_address_query.count()
        address = total - no_address
        percentage_address = round((100*address)/total, 1)

        #PHONE STATISTICS
        no_phone_number = Leadership.objects.filter(phone_number='') | \
            Leadership.objects.filter(phone_number=None)
        no_cellphone = Leadership.objects.filter(cellphone='') | \
            Leadership.objects.filter(cellphone=None)
        no_phone_home = Leadership.objects.filter(phone_home='') | \
            Leadership.objects.filter(phone_home=None)

        no_phone_query = no_phone_number.intersection(no_cellphone).intersection(no_phone_home)
        no_phone = no_phone_query.count()
        phone = total - no_phone
        percentage_phone = round((100*phone)/total, 1)

        #EMAIL STATISTICS
        no_email = Leadership.objects.filter(email='') | Leadership.objects.filter(email=None)
        email = total - no_email.count()
        percentage_email = round((100*email)/total, 1)

        # BIRTH STATISTICS
        birth = Leadership.objects.exclude(birth=None).count()
        percentage_birth = round((100*birth)/total, 1)
        
        leadership = {'total': total,
                    'address': address,
                    'percentage_address': percentage_address,
                    'phone': phone,
                    'percentage_phone':percentage_phone,
                    'email': email,
                    'percentage_email': percentage_email,
                    'birth': birth,
                    'percentage_birth': percentage_birth}
        return leadership

    def statistic_authorities(self):
        total = Authoritie.objects.count()

        #PHONE STATISTICS
        no_phone_number = Authoritie.objects.filter(phone_number='') | \
            Authoritie.objects.filter(phone_number=None)
        # no_cellphone = Authoritie.objects.filter(cellphone='') | \
        #     Authoritie.objects.filter(cellphone=None)
        # no_phone_home = Authoritie.objects.filter(phone_home='') | \
        #     Authoritie.objects.filter(phone_home=None)

        #no_phone_query = no_phone_number.intersection(no_cellphone).intersection(no_phone_home)
        #no_phone = no_phone_query.count()
        phone = total - no_phone_number.count()
        percentage_phone = round((100*phone)/total, 1)

        authorities = {'total': total,
                        'phone': phone,
                        'percentage_phone': percentage_phone}

        return authorities
        