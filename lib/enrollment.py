from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            # Prevent duplicate enrollments
            if not any(enrollment.course == course for enrollment in self._enrollments):
                enrollment = Enrollment(self, course)
                self._enrollments.append(enrollment)
                course.add_enrollment(enrollment)
            else:
                print(f"{self.name} is already enrolled in {course.title}.")
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def __str__(self):
        return f"Student(name={self.name})"


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def __str__(self):
        return f"Course(title={self.title})"


class Enrollment:
    all = []  
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    @property
    def enrollment_date(self):
        return self._enrollment_date  

    def __str__(self):
        return f"Enrollment(student={self.student.name}, course={self.course.title}, date={self._enrollment_date})"
