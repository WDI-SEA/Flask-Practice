class Assignment():
    def __init__(self, name, github_url):
        self.name = name
        self.github_url = github_url
        self.completed = False
        self.grade = None
    def mark_done(self, grade):
            self.grade = grade
            self.completed = True

class Student():
    def __init__(self, name):
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []
    def assign_homework(self, thisAssignment):
            self.pending_homeworks.append(thisAssignment)
    def complete_homework(self, assignmentName, grade):
            found = False
            for assignment in self.pending_homeworks:
                if (assignment.name == assignmentName):
                    found = True
                    self.pending_homeworks.remove(assignment)
                    assignment.mark_done(grade)
                    self.completed_homeworks.append(assignment)
            return found
    def print_outstanding_homeworks(self):
            if len(self.pending_homeworks):
                for assignment in self.pending_homeworks:
                    print(f'{self.name} still has to turn in {assignment.name}')
            else:
                print(f'{self.name} has no outstanding homeworks')

class SeiClass():
    def __init__(self, name):
        self.name = name
        self.students = []
    def assign_homework(self, assignment):
            for student in self.students:
                student.assign_homework(assignment)
    def add_student(self, student):
            self.students.append(student)
    

nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

nick.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()