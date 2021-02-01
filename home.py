class students:
    #class variable number_of_students denoting the number of students....updated each time a student is created
    number_of_students = 0
    def __init__(self,name,age,gender,class_):
        #here is specified the instance variables name,age,gender,class_
        self.name = name
        self.age = age
        self.gender = gender
        self.class_ = class_
        #here we update the class variable number_of_students each time an instance is created 
        students.number_of_students += 1
    @classmethod
    #this is a class method for creating/constructing students from a string of information given and returns the student(name,age,gender,class_)
    def create_student_profile(cls,student_info):
        student_info = student_info.split('-')
        name, age, gender, class_ = student_info[0], student_info[1], student_info[2], student_info[3]
        return cls(name, int(age), gender, class_)
    @staticmethod
    #this is a static method that shows the  number of books needed by students of a particular level i.e O and A level.
    #note that there is no argument of cls(class) or self(instance) passed
    def number_of_books(class_):
         return 12 if class_<= 4 else 16
    #now we'll create  students and show the effect of all the methods
stdt_1 = students.create_student_profile('Kissa Leon Denis-18-Male-6')
stdt_2 = students.create_student_profile('Muliika Fahad-19-Male-6')
stdt_3 = students.create_student_profile('Nagujja Rosler-16-Female-4')
stdt_4 = students.create_student_profile('Akisa Christa-15-Female-3')
stdt_5 = students.create_student_profile('Kantu Iris-18-Female-6')
stdt_6 = students.create_student_profile('Malinga Milly Ketty-19-Female-6')
stdt_7 = students.create_student_profile('Arikod Edwine-19-Male-6')
    
print('number of students(using instance):',stdt_1.number_of_students,'\n')
print('number of students(using class):',students.number_of_students,'\n')
list_of_students = [stdt_1,stdt_2,stdt_3,stdt_4,stdt_5,stdt_6,stdt_7]
for stdt in list_of_students:
    print('Name: {}\nClass: {}\nGender: {}\nNumber of books needed: {}\nNumber of students: {}\n'.format(stdt.name,stdt.class_,stdt.gender,stdt.number_of_books(int(stdt.class_)),stdt.number_of_students))
#Have fun playing with what I've made here.... :)     