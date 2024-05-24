class Student:
    def __init__(self, stuName, stuAge, stuGrade):
        self.name = stuName; self.age = stuAge; self.grade = stuGrade; #grades from 0 - 100
    
    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, courseName, courseMaxStrength):
        self.name = courseName; self.MaxStrength = courseMaxStrength; self.studentsAllocated = [];
        
    def addStudents(self, student):
        if (len(self.studentsAllocated) < self.MaxStrength):
            self.studentsAllocated.append(student)
            print("Adding student successful")
        else:
            print("Adding student failed since course maximum strength exceeded")
        
    def getAvgGrade(self):
        sum = 0
        for student in self.studentsAllocated:
            sum += student.getGrade()
        return (sum / len(self.studentsAllocated))
    
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jack", 20, 65)

c1 = Course("Computer Science 101", 2)
c1.addStudents(s1); c1.addStudents(s2); c1.addStudents(s3);
print("\nThe Average Grade to ", c1.name," is - ", c1.getAvgGrade())