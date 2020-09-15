from employees.models import Employee
from positions.models import Position
from institutions.models import Institution
from authorities.models import Authoritie
from parties.models import Party
from leadership.models import Leadership
from candidates.models import Candidate
from customers.models import Customer
from solicitations.models import Solicitation
from datetime import datetime
import csv

def to_datetime(date):
        date_list = date.split("/")
        date_converted = '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])
        return datetime.strptime(date_converted, '%Y-%m-%d')

def to_datetime_inverted(date):
    date_list = date.split("/")
    if int(date_list[2]) < 20:
        year = "20{}".format(date_list[2])
    else:
        year = "19{}".format(date_list[2])
    date_converted = '{}-{}-{}'.format(year, date_list[0], date_list[1])
    return datetime.strptime(date_converted, '%Y-%m-%d')

def funcionario():
    file = open("/maladireta/database/funcionarios.csv")
    count = 0
    for line in file.readlines():
        dados = line.split(',')
        employee = Employee()
        for i in range(len(dados)):
            if i == 1:
                employee.name = dados[i]
            elif i == 2:
                employee.nickname = dados[i]
            elif i == 3:
                employee.phone_number = dados[i]
            elif i == 4:
                employee.cellphone = dados[i]
            elif i == 5:
                employee.street = dados[i]
            elif i == 6:
                employee.neighborhood = dados[i]
            elif i == 7:
                employee.city = dados[i]
            elif i == 8:
                employee.cep = dados[i]
            elif i == 9:
                employee.email = dados[i]
            elif i == 10:
                employee.function = dados[i]
            elif i == 12:
                employee.note = dados[i]
            elif i == 14:
                employee.birth = to_datetime(date = dados[i]) 
            elif i == 15:
                employee.state = dados[i]
            elif i == 17:
                employee.number = dados[i].split("\n")[0]
            employee.save()
            count = count + 1
    print("{} funcionários adicionados".format(count))

def cargo():
    file = open("/maladireta/database/cargos.csv")
    count = 0
    for line in file.readlines():
        dados = line.split(',')
        position = Position()
        for i in range(len(dados)):
            if i == 1:
                position.position = dados[i]
            elif i == 2:
                position.handling = dados[i]
            elif i == 3:
                position.abbreviation = dados[i]
            position.save()
            count = count + 1
    print("{} cargos adicionados".format(count))

def instituicao():
    with open('/maladireta/database/instituicoes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                telefone = None
                if row[2]:
                    telefone = ''.join((filter(lambda x: x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '-', '/'], row[2])))
                institution = Institution()
                institution.name = row[1]
                query = Institution.objects.search(institution.name)
                if not query:
                    institution.phone_number = telefone
                    institution.street = row[3]
                    institution.city = row[4]
                    institution.number = row[5]
                    institution.neighborhood = row[7]
                    institution.cep = row[8]
                    institution.state = row[9]
                    institution.note = row[11]
                    institution.save()
                    #print(f'\tNome: {row[1]}\nTelefones {telefone}\nEndereço: {row[3]}\nCidade: {row[4]}\nNumero: {row[5]}\nComplemento: {row[6]}\nBairro: {row[7]}\nCEP: {row[8]}\nUF: {row[9]}\nOBS: {row[11]}')
                    line_count += 1
    print(f'{line_count} instituições adicionadas.')

def autoridade():
    with open('/maladireta/database/autoridades.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        position_count = 0
        institution_count = 0
        authoritie_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[3]:
                    ### Position
                    if not row[4]:
                        row[4], row[5] = "Vossa Senhoria", "V. S.ª"
                    
                    position = Position()
                    position.position, position.handling, position.abbreviation = row[3], row[4], row[5]
                    position_query = Position.objects.search(position.position)
                    if not position_query:
                        position.save()
                        position_count += 1
                    
                    ## Institution
                    if row[6]:
                        telefone = None
                        if row[7]:
                            telefone = ''.join((filter(lambda x: x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '-', '/'], row[7])))

                        institution = Institution()
                        institution.name = row[6]
                        institution.phone_number = telefone
                        institution.city = row[8]
                        institution.street = row[9]
                        institution.number = row[10]
                        institution.complement = row[11]
                        institution.neighborhood = row[12]
                        institution.cep = row[13]
                        institution.state = row[14]
                        institution.note = row[15]
                        institution_query = Institution.objects.search(institution.name)
                        if not institution_query:
                            institution.save()
                            institution_count += 1
                    
                    ### Authoritie
                    if row[16]:
                        authoritie = Authoritie()
                        authoritie.name = row[16]
                        if row[19]:
                            authoritie.birth = to_datetime_inverted(row[19].split(' ')[0])
                        authoritie.position = Position.objects.search(position.position)[0]
                        authoritie.institution = Institution.objects.search(institution.name)[0]
                        authoritie_query = Authoritie.objects.search(authoritie.name)
                        if not authoritie_query:
                            authoritie.save()
                            authoritie_count += 1

    return authoritie_count, institution_count, position_count

def partido():
    with open('/maladireta/database/partidos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        party_count = 0
        leadership_count = 0
        position = Position.objects.search("Presidente de Partido")[0]
        print(position)
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if not Party.objects.search(row[1]):
                    print(row[1])
                    party = Party()
                    party.initials = row[1]
                    party.number = row[2]
                    party.name = row[3]
                    party.union = row[4]

                    if row[5]:
                        leadership = Leadership()
                        leadership.name = row[5]
                        leadership.street = row[6]
                        leadership.number = row[7]
                        leadership.neighborhood = row[8]
                        leadership.city = row[9]
                        leadership.state = row[10]
                        leadership.cep = row[11]
                        leadership.note = row[12]
                        leadership.email = row[13]
                        leadership.complement = row[14]
                        leadership.position = position
                        leadership.save()
                        leadership_count += 1
                        party.leadership = Leadership.objects.search(leadership.name)[0]

                    party.save()
                    party_count += 1
    return party_count, leadership_count

def candidato():
    with open('/maladireta/database/candidatos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                candidate = Candidate()
                candidate.name = row[0]
                candidate.number = row[1]
                party_query = Party.objects.search(row[2])
                if party_query:
                    candidate.party = party_query[0]
                else:
                    print(candidate.name)
                if row[4] == 'DE':
                    candidate.position = Position.objects.search('Deputado Estadual')[0]
                elif row[4] == 'DF':
                    candidate.position = Position.objects.search('Deputado Federal')[0]
                elif row[4] == 'G':
                    candidate.position = Position.objects.search('Governador')[0]
                elif row[4] == 'S':
                    candidate.position = Position.objects.search('Senador')[0]
                candidate.save()    
    return line_count -1

def cliente():
    with open('/maladireta/database/clientes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
                line_count += 1
            elif line_count == 1:
                customer = Customer()
                customer.name = row[0]
                if row[1]:
                    customer.birth = to_datetime_inverted(row[1].split(' ')[0])
                customer.nickname = row[2]
                customer.reference = row[3]
                customer.state = row[4]
                customer.cep = row[5]
                customer.old_id = row[10]
                customer.note = row[11]
                customer.cpf = row[12]
                customer.rg = row[13]
                customer.phone_home = row[14]
                customer.phone_number = row[15]
                customer.cellphone = row[16]
                customer.complement = row[17]
                customer.street = row[18]
                customer.leadership = row[20]
                customer.location_reference = row[21]
                customer.number = row[26]
                customer.email = row[27]
                customer.profession = row[28]
                customer.neighborhood = row[29]
                customer.city = row[30]
                customer.recurrence = row[32]
                customer.subscription = row[38]
                customer.zone = row[39]
                customer.section = row[40]
                customer.save()
            else:
                break
                
def exclui_clientes():
    for customer in Customer.objects.all():
        customer.delete()

def lideranca():
    with open('/maladireta/database/liderancas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
                line_count += 1
            elif line_count == 1:
                leadership = Leadership()
                leadership.name = row[1]
                if row[3]:
                    leadership.birth = to_datetime_inverted(row[3].split(' ')[0])
                leadership.rg = row[4]
                leadership.cpf = row[5]
                leadership.nickname = row[6]
                if row[8]:
                    position_query = Position.objects.search(row[8])
                    if position_query:
                        leadership.position = position_query[0]
                    else:
                        leadership.office = row[8]
                leadership.neighborhood = row[10]
                leadership.city = row[11]
                leadership.state = row[12]
                leadership.cep = row[13]
                leadership.phone_home = row[14]
                leadership.phone_number = row[15]
                leadership.cellphone = row[16]
                leadership.email = row[17]
                leadership.street = row[19]
                leadership.number = row[23]
                leadership.pendency = row[24]
                leadership.note = row[25]
                leadership.save()

def pleito():
    with open('/maladireta/database/pleitos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        without_customer = 0
        with_customer = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
            else:
                customer_query = Customer.objects.filter(old_id=row[1])
                if customer_query and len(customer_query) == 1:
                    solicitation = Solicitation()
                    solicitation.description = row[3]
                    solicitation.customer = customer_query[0]
                    solicitation.note = row[5]
                    solicitation.indication = row[7]
                    if row[10]:
                        solicitation.value = row[10]
                    solicitation.situation = row[11]
                    solicitation.historic = row[13]
                    solicitation.save()
                else:
                    print(f'{", ".join(row)}')
            line_count += 1

def exclui_pleitos():
    for solicitation in Solicitation.objects.all():
        solicitation.delete()
