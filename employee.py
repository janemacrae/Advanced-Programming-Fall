class Employee:
   'Common base class for all employees'
   janitorCount = 0
   ceoCount = 0

   def __init__(self, name, salary, title):
      self.name = name
      self.salary = salary
      self.title = title
      Employee.janitorCount += 1
      Employee.ceoCount += 1

   def displayCount(self):
     print "Total Janitor %d" % Employee.janitorCount
     print "Total CEO %d" % Employee.ceoCount

   def displayEmployee(self):
      print "Name : ", self.name, ", Salary: ", self.salary, "Title : ", self.title

"This would create first object of Employee class"
emp1 = Employee("Ishmael", 10, "Janitor")
"This would create second object of Employee class"
emp2 = Employee("Jane", 100000000, "CEO")
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Janitor %d" % Employee.janitorCount
print "Total CEO %d" % Employee.ceoCount
