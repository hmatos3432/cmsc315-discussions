Unit 1 Discussion: Python OOP, Namespaces, and Copying
Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

Learning Objectives
Create parent and child classes
Use inheritance to extend functionality
Understand class and instance namespaces
Demonstrate shallow and deep copying
Apply object-oriented design principles
Requirements

Complete all TODO sections in the source code:

Create a parent class.
Create a child class using inheritance.
Demonstrate class and instance namespaces.
Demonstrate shallow and deep copying.
Create and test objects in main().
Add a student-created extension.
Implementation Documentation
Parent Class

I created a parent class named ParentClass. The class included the class variable species and the instance variables name and age. I used the __init__() constructor to initialize each object. I also created a display_info() method that returned the object's name and age.

Child Class and Inheritance

I created a child class named ChildClass that inherited from ParentClass. The child class added the class variable school_name and the instance variables student_id and courses.

I used super().__init__() to reuse the parent constructor instead of repeating the code used to initialize name and age. I also added an add_course() method and overrode the display_info() method so that student-specific information could be displayed.

Class and Instance Namespaces

I demonstrated class and instance namespaces by creating two ChildClass objects. I accessed the school_name class variable through both the class itself and an individual object.

I also added a major attribute to only one student after the object was created. I used __dict__ to display each object's namespace and show that the new attribute existed only in that specific object. I also displayed the ChildClass namespace to demonstrate the difference between class-level and instance-level attributes.

Shallow and Deep Copying

I demonstrated shallow and deep copying using the mutable courses list.

I created a shallow copy using copy() and a deep copy using deepcopy(). After creating both copies, I added another course to the original student's course list.

The shallow copy reflected the change because it shared the same nested mutable course list with the original object. The deep copy remained unchanged because it contained its own independent copy of the list.

Student-Created Extension

I added a remove_course() method to ChildClass as my student-created extension.

The method checked whether a requested course existed in the student's courses list before attempting to remove it. If the course existed, the method removed it and returned a confirmation message. If the course was not found, the method returned a message instead of causing an error.

Testing and Edge Cases

I tested the program by creating both parent and child objects, adding multiple courses, accessing inherited variables, removing courses, displaying namespaces, and comparing shallow and deep copies.

I also added additional test cases beyond the basic requirements. I attempted to remove CMSC 999, which was not included in the student's course list. The program correctly returned a message stating that the course was not found instead of producing an error.

I also created a student without adding any courses. The program displayed an empty course list as []. This demonstrated that the program could handle an empty mutable structure without crashing.

Real-World Application

This design could be applied to a student enrollment system used by a university. The parent class could store information shared by people in the system, such as a person's name and age. The child class could represent students and contain additional information such as student IDs and enrolled courses.

Inheritance would reduce repeated code by allowing student objects to reuse information and methods from the parent class. The mutable courses list could also grow or shrink as students enrolled in or dropped courses. This design could later be expanded to include instructors, departments, course schedules, and enrollment records.

Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

What concepts or skills did you learn while completing this assignment?
What challenges did you encounter, and how did you overcome them?
Compare OOP to procedural programming.
Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.