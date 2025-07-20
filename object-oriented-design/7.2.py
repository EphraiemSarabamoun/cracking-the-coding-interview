import random
import enum
import time

class Level(enum.IntEnum):
    Respondent = 0
    Manager = 1
    Director = 2

class Employee:
    def __init__(self, level,id):
        self.level = level
        self.is_available = True
        self.id = id
    def call(self,call):
        self.is_available = False
        time.sleep(1)
        if random.random() < 0.9:
            call.end()
        else:
            call.escalate()
        self.is_available = True
        return

class Call:
    def __init__(self):
        self.level = Level.Respondent
        self.ended = False

    def end(self):
        self.ended = True
        return
    def escalate(self):
        if self.level == Level.Director:
            self.end()
        self.level = Level(self.level + 1)
        return

class Call_Center:
    def __init__(self):
        self.employees = {"Respondent": [Employee(Level.Respondent, i) for i in range(1,6)], "Manager": [Employee(Level.Manager, i) for i in range(6,8)], "Director": [Employee(Level.Director, i) for i in range(8,9)]}
    def dispatch_call(self,call):
        if call.level == Level.Respondent:
            for employee in self.employees["Respondent"]:
                if employee.is_available:
                    employee.call(call)
                else:
                    for employee in self.employees["Manager"]:
                        if employee.is_available:
                            employee.call(call)
                        else:
                            for employee in self.employees["Director"]:
                                if employee.is_available:
                                    employee.call(call)
                                else:
                                    call.end()
        if call.level == Level.Manager:
            for employee in self.employees["Manager"]:
                if employee.is_available:
                    employee.call(call)
                else:
                    for employee in self.employees["Director"]:
                        if employee.is_available:
                            employee.call(call)
                        else:
                            call.end()
        if call.level == Level.Director:
            for employee in self.employees["Director"]:
                if employee.is_available:
                    employee.call(call)
                else:
                    call.end()

if __name__ == "__main__":
    call_center = Call_Center()
    call = Call()
    call_center.dispatch_call(call)

        
