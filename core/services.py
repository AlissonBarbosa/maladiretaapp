from employees.models import Employee
from positions.models import Position
from datetime import datetime

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