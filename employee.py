import math


class Employee:
    def __init__(self, emp_id, fname, lname, salary):
        self.emp_id = emp_id
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __str__(self):
        return f"Employee(ID: {self.emp_id}, Name: {self.fname} {self.lname}, Salary: {self.salary})"

    def __repr__(self):
        return f"Employee(ID: {self.emp_id}, Name: {self.fname} {self.lname}, Salary: {self.salary})"

    def __eq__(self, other):
        return (
            isinstance(other, Employee) and
            self.emp_id == other.emp_id and
            self.fname == other.fname and
            self.lname == other.lname and
            self.salary == other.salary
        )

    def __hash__(self):
        return hash( ( self.emp_id, self.fname,  self.lname, self.salary) )

e1 = Employee(1, 'a', 'b', 3)
print(e1)
print('hash(e1)', hash(e1))
e2 = Employee(1, 'a', 'b', 3)
print(e2)
print('hash(e2)', hash(e2))
print('e1 == e2', e1 == e2)
d = dict({e1: 3})
d[e2] = 2
print(d)
print('hash e1', hex(hash(e1)))
print('hash e2', hex(hash(e2)))

# if 2 elements are __eq__ they should have the same hash
# if you rewrite the __eq__ you must rewrite the hash function


