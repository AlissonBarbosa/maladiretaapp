from employees.models import Employee
from positions.models import Position
from institutions.models import Institution
from authorities.models import Authoritie
from datetime import datetime
import csv

def to_datetime(date):
        date_list = date.split("/")
        date_converted = '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])
        return datetime.strptime(date_converted, '%Y-%m-%d')

def to_datetime_inverted(date):
    date_list = date.split("/")
    print(date_list)
    year = '2020'
    date_converted = '{}-{}-{}'.format(year, date_list[0], date_list[1])
    return datetime.strptime(date_converted, '%Y-%m-%d')

def funcionario():
    file = open("/home/alisson/Workspace/maladireta/database/funcionarios.csv")
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
    file = open("/home/alisson/Workspace/maladireta/database/cargos.csv")
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
    with open('/home/alisson/Workspace/maladireta/database/instituicoes.csv') as csv_file:
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
    with open('/home/alisson/Workspace/maladireta/database/autoridades.csv') as csv_file:
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
                        

        
