"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    school_name = "Generic University"

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)

    # STUDENT-CREATED EXTENSION:
    # Removes a course if it exists and safely handles a missing course.
    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            return f"{course_name} removed."
        return f"{course_name} not found."

    # Overrides display_info() from ParentClass.
    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, "
            f"School: {self.school_name}, "
            f"Courses: {self.courses}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Hector", 33, "S001")
    student2 = ChildClass("Alex", 25, "S002")

    # Access the class variable through the class.
    print("Class variable through class:", ChildClass.school_name)

    # Access the same class variable through an object.
    print("Class variable through object:", student1.school_name)

    # Add a new attribute to only one object.
    student1.major = "Computer Science"

    # Display each object's instance namespace.
    print("Student 1 namespace:", student1.__dict__)
    print("Student 2 namespace:", student2.__dict__)

    # Display information about the class namespace.
    print("ChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # The courses list is mutable data stored inside the object.
    original_student = ChildClass("Hector", 33, "S003")
    original_student.add_course("CMSC 315")

    # A shallow copy creates a new outer object, but nested mutable
    # objects such as the courses list are still shared.
    shallow_student = copy(original_student)

    # A deep copy creates a completely independent copy, including
    # the nested mutable courses list.
    deep_student = deepcopy(original_student)

    # Modify the original object's nested mutable data.
    original_student.add_course("CMSC 320")

    print("Original:", original_student.display_info())
    print("Shallow Copy:", shallow_student.display_info())
    print("Deep Copy:", deep_student.display_info())


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a ParentClass object.
    print("\n=== Parent Object ===")
    parent = ParentClass("Hector", 33)
    print(parent.display_info())

    # Create and test a ChildClass object.
    print("\n=== Child Object ===")
    student = ChildClass("Hector", 33, "S001")
    student.add_course("CMSC 315")
    student.add_course("CMSC 320")
    print(student.display_info())

    # Demonstrate inheritance from ParentClass.
    print("Inherited species:", student.species)

    # Test the student-created extension.
    print("\n=== Student-Created Extension ===")
    print(student.remove_course("CMSC 320"))
    print(student.display_info())

    # Additional edge-case test:
    # Attempt to remove a course that does not exist.
    print("\n=== Edge Case Test ===")
    print(student.remove_course("CMSC 999"))

    # Additional test for an empty mutable list.
    empty_student = ChildClass("Jordan", 20, "S004")
    print("Student with no courses:", empty_student.display_info())

    # Run the required demonstrations.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()