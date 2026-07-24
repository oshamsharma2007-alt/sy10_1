class Student:
    school_name = "MIT ADT University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "scored", self.marks)

    @staticmethod
    def is_pass(marks):
        return marks >= 40

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"


s1 = Student("Aman", 85)
s2 = Student("Riya", 92)

print(s1.name, s1.marks, s1.school_name)
print(s2.name, s2.marks, s2.school_name)

s1.show()

print(Student.is_pass(30))
print(Student.is_pass(85))

print(s1)
print(s2)


def announce(func):
    def wrapper(*args, **kwargs):
        print(">>> Starting...")
        result = func(*args, **kwargs)
        print(">>> Done!")
        return result
    return wrapper


@announce
def check_result(student):
    if Student.is_pass(student.marks):
        print(student.name, "PASSED")
    else:
        print(student.name, "FAILED")


check_result(s1)
check_result(s2)


class RollNumbers:
    def __init__(self, max_roll):
        self.max_roll = max_roll

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        if self.current <= self.max_roll:
            x = self.current
            self.current += 1
            return x
        else:
            raise StopIteration


for roll in RollNumbers(5):
    print("Roll No:", roll)


def roll_numbers(max_roll):
    current = 1
    while current <= max_roll:
        yield current
        current += 1


for roll in roll_numbers(5):
    print("Roll No:", roll)
