class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_teamlead():
    teamlead = TeamLead(name="Kavun", salary=100000, department="Engineering", programming_language="Python", team_size=10)


    assert teamlead.name == "Kavun"
    assert teamlead.salary == 100000
    assert teamlead.department == "Engineering"
    assert teamlead.programming_language == "Python"
    assert teamlead.team_size == 10

print("idk")
test_teamlead()



