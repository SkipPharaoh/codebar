# Write your code here!


class Member:
    def __init__(self, full_name):
        self.name = full_name

    def introduce(self):
        print(f"Fancy meeting you, my name is {self.name}!")

skip = Member("Caniggia Thompson")
# print(skip.name)

skip.introduce()


class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

derek = Student("Derek", "I've always wanted to make websites!")
# print(derek.reason)


class Instructor(Member):
    def __init__(self, full_name, bio, skills=[]):
        super().__init__(full_name)
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

henry = Instructor("Henry Hong", "I've been coding in Python for 5 years and want to share the love!", ["Python", "Javascript", "C++"])
josh = Instructor("Joshua Smith", "I've been coding in Python for 5 years and want to share the love!", ["Python", "Javascript", "C++"])

henry.add_skill("Ruby")
# print(henry.skills)


class Workshop:
    def __init__(self, date, subject, instructors=[], students=[]):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, member):
        if member.__class__.__name__ == "Instructor":
            self.instructors.append(member.name)
        elif member.__class__.__name__ == "Student":
            self.students.append(member.name)

    def print_details(self):
        print(self.__dict__)

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

print(vicky.skills)
print(nicole.skills)

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
