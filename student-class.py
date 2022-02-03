# create  a class named student with the attributes name, age and class
# class has default value 'student'
# Then also give it a method that takes the average of 3 test scores

class Student:
    def __init__(self, name, age, class_='student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def avgscore(self, score1, score2, score3):
        sum = (int(score1) + int(score2) + int(score3))
        avg = sum / 3
        return avg


Example = Student('Example', 17, '2E')
print(Example.avgscore(15, 20, 25))
