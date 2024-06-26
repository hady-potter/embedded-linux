import csv
import uuid


embloyees = []

def menu():
  print('1) Add New Employee')
  print('2) Print All Employees')
  print('3) Remove Employee')
  print('4) Update Employee')
  print('5) quit')
  print('=' * 30)

class Embloyee:
  def __init__(self, name, job, salary):
    self.name = name
    self.job = job
    self.salary = salary
    self.id = uuid.uuid1()

  def add_employee(self, embloyee):
    embloyees.append(embloyee)

  @staticmethod
  def print_all_embloyees():
    for embloyee in embloyees:
      print('\tname:', embloyee.name)
      print('\tjob:', embloyee.job)
      print('\tSalary:', embloyee.salary)
      print('\tID:', embloyee.id)
      print('=' * 30)

  def remove_employee(self):
    for embloyee in embloyees[:]:
      if str(id) == str(embloyee.id):
        embloyees.remove(embloyee)
        break

  def update_employee(self, embloyee_id):
    for embloyee in embloyees:
      if str(embloyee.id) == str(embloyee_id):
        embloyee.name = name
        embloyee.job = job
        embloyee.salary = salary



menu()

while(True):
  ans = input('Answer: ')
  match ans:
    case '1':
      name = input('name: ')
      job = input('jop: ')
      salary = input('salary: ')
      embloyee = Embloyee(name, job, salary)
      embloyee.add_employee(embloyee)

    case '2':
      print('=' * 30)
      Embloyee.print_all_embloyees()

    case '3':
      id = input('id: ')
      embloyee = Embloyee('name', 'job', 12)
      embloyee.remove_employee()

    case '4':
      old_embloyee_id = input('id of embloyee you want to update: ')
      name = input('new name: ')
      job = input('new jop: ')
      salary = input('new salary: ')
      embloyee = Embloyee(name, job, salary)
      embloyee.update_employee(old_embloyee_id)

    case _:
      print('Done')
      break


with open('database.csv', 'a') as f:
  embloyee = []
  writer = csv.writer(f)
  for e in embloyees:
    embloyee.append([e.name, e.job, e.salary, e.id])
  

  writer.writerows(embloyee)

print('DONE')


