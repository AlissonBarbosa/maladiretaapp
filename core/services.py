from employees.models import Employee
from positions.models import Position
from institutions.models import Institution
from datetime import datetime
import csv

def to_datetime(date):
        date_list = date.split("/")
        date_converted = '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])
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
        
