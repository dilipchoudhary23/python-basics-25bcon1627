class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Creating a student object
s1 = Student("Rahul", 101, 85)

# Display student details
s1.display()
